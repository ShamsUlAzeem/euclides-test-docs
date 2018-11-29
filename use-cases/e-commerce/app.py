import json
from io import BytesIO

import euclides
import flickrapi
import numpy as np
import requests
from PIL import Image
from flask import Flask
from flask import render_template
from flask import request
from torchvision.transforms import functional as f

api_key = u'08a4c9520038b3e91424eae6e62b8a4a'
api_secret = u'a219f8055bf83fcc'

app = Flask(__name__)


@app.route('/recommend', methods=['GET'])
def recommend():
    image_url = request.args.get('url')

    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    image_id = int(1)
    image.thumbnail((300, 300), Image.ANTIALIAS)
    image = f.center_crop(image, 224)

    with euclides.Channel("localhost", 8000) as channel:
        db = euclides.EuclidesDB(channel)
        ret_add = db.add_image(image_id, ["resnet18"], image)

        # After finishing adding items, you need to tell
        # the database to refresh the indexes to add newly
        # indexed items.
        db.refresh_index()

    predictions = ret_add.vectors[0].predictions
    print("Preds Len: ", len(predictions))

    labels = requests.get("https://gist.githubusercontent.com/ShamsUlAzeem/3ea5740b960d854f4bd43e7322b858e3/raw"
                          "/e8e3d428fb94af3c1c20beea9183de364ecbc3a5/imagenet-labels.json").json()

    category = np.array(predictions).argmax()

    output = labels[str(category)]

    images = []
    for name in output.split(","):
        images.extend(find_images(name))

    return render_template('show_images.html', images=images, output=output, url=image_url)


def find_images(search_string):
    page_index = 1
    images_per_page = 2
    flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')
    sets = flickr.photos.search(text=search_string, page=str(page_index),
                                per_page=str(images_per_page))

    # totalImages = int(sets['photos']['total'])

    # https://farm{farm-id}.staticflickr.com/{server-id}/{id}_{secret}.jpg
    url_format_1 = "https://farm{}.staticflickr.com/{}/{}_{}.jpg"

    photos = sets['photos']['photo']

    image_links = []

    for i in range(len(photos)):
        photo = photos[i]
        farm_id = photo['farm']
        server_id = photo['server']
        image_id = photo['id']
        secret = photo['secret']

        # Using url format 1 to format image url
        image_url = url_format_1.format(farm_id, server_id, image_id, secret)
        image_links.append(image_url)

    return image_links


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

To run the app you should have the following softwares installed:
1. [Python (2 or 3)](https://www.python.org/downloads/)
2. [PyTorch](https://pytorch.org/get-started/locally/)
3. [Docker](https://docs.docker.com/install/#supported-platforms)
4. [Git](https://www.linode.com/docs/development/version-control/how-to-install-git-on-linux-mac-and-windows/)

## Running the Application

Run the EuclidesDB from the docker container:
```bash
docker run -p 8000:50000 -it --name euclidesdb euclidesdb/euclidesdb
```

Clone the repository
```bash
git clone https://github.com/ShamsUlAzeem/euclides-test-docs.git
```

Switch directories
```bash
cd euclides-test-docs/use-cases/e-commerce
```

Install the python dependencies
```bash
pip install -r requirements.txt
```

Run the app
```bash
python app.py
```

## Testing the Application

The *EuclidesDB* server would be running on port `8000` on localhost, serving **ResNet18**, while the flask web application would be running on port `5000`. To interact with the application, navigate to the following url:
`http://localhost:5000/recommend?url=<your_image_url>`

Replace `<your_image_url>` with an image URL you wanna get recommendations for. For example, `http://localhost:5000/recommend?url=https://farm5.staticflickr.com/4908/44265208170_24c0da35d1_q_d.jpg`. The app will load the image, run it through the classifier and get recommendations for you via the flickr API.

## SAMPLE
![Sample](sample.jpg?raw=true "Sample image")


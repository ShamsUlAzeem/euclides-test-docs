This walkthrough will guide your through the :ref:`installation` and :ref:`configuration` process for setting up *EuclidesDB*.

.. _installation:

============
Installation
============

Pre-requisites
--------------
Before installing *EuclidesDB*, make sure you have an appropriate version of `PyTorch <https://pytorch.org/get-started/locally/>`_ installed on your system. It is required for `saving <https://pytorch.org/tutorials/beginner/saving_loading_models.html>`_ your custom models for configurations inside *EuclidesDB*.

.. _all-os:

All Operating Systems
---------------------
The easiest and quickest way to get *EuclidesDB* up and running is through a `Docker <https://docs.docker.com/install/>`_ container. To start a *EuclidesDB* container execute the following commands in a terminal:

.. code-block:: shell

    docker volume create --name edb
    docker run -p 50000:50000 --mount source=edb,target=/database -it --name euclidesdb euclidesdb/euclidesdb

This will create a docker `volume <https://docs.docker.com/storage/volumes/>`_ to save the default database configurations and start the *EuclidesDB* server, serving a pre-configured PyTorch ResNet-18 model with the DB.

.. note::

    If the database doesn’t exists, it will be created by EuclidesDB on the first run.

Linux
-----
To install *EuclidesDB* on a Linux systems, download the `lastest <https://github.com/perone/euclidesdb/releases>`_ Linux release from the github repository, extract it and run the database server as follows:

.. code-block:: shell

    wget https://github.com/perone/euclidesdb/releases/download/v0.1.1/euclidesdb-0.1.1-Linux.tar.gz
    tar zxvf euclidesdb-0.1.1-Linux.tar.gz
    cd euclidesdb
    ./euclidesdb -c euclidesdb.conf

.. note::

    At the time of this writing, the latest version was `0.1.1`.

The Linux tarball distributions comes with all the dependencies packaged to work out of the box.

Mac OS
------
To install EuclidesDB in MacOS, the best approach is to install dependencies using `homebrew <https://brew.sh/>`_ as shown below:

.. code-block:: shell

    brew install grpc
    brew install leveldb
    brew install libomp

Download the `lastest <https://github.com/perone/euclidesdb/releases/latest>`_ Mac OS release and install it:

.. code-block:: shell

   curl -L -o 'euclidesdb-0.1.1-Darwin.dmg' 'https://github.com/perone/euclidesdb/releases/download/v0.1.1/euclidesdb-0.1.1-Darwin.dmg'
   hdiutil attach euclidesdb-0.1.1-Darwin.dmg
   cp -R /Volumes/euclidesdb-0.1.1-Darwin\euclidesdb .
   hditutil detach /Volumes/euclidesdb-0.1.1-Darwin/
   cd euclidesdb
   ./euclidesdb -c euclidesdb.conf

.. note::

    At the time of this writing, the latest version was `0.1.1`.

Windows
-------
For windows, *EuclidesDB* can only be used through a docker container. Please refer to :ref:`all-os`.

------------

.. _configuration:

=============
Configuration
=============

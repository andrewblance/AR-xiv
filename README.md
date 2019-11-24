# AR-xiv

Simple Hololens v1 app. Features a cube you can boop - doing so turns on gravity. Also here is a small program that will query the arXiv and return the latest HEP papers. Currently, these two parts are crudely linked.

Made using:

* Unity 2018.4.10f1
* VS community 2019 v16.3.2

For the Docker:

* docker build -t arxiv:latest .
* docker run -d -p 5000:5000 arxiv

Then, you can access the arXiv Grabber from localhost:5000

#!/bin/bash

#  pull docker image
docker pull yash6370/simple-flask-app
#  run simple flask application
docker run -d -p 80:5000 --name simple-flask-app yash6370/simple-flask-app
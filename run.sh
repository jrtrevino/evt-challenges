#! /bin/sh
docker build -t my-web-server-image .
docker run -p 4443:4443 my-web-server-image
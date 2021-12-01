#! /bin/sh
# prepare directory
rm -rf web
# clone index page
git clone https://bitbucket.org/bjgiller/evt-tech-challenge/raw/master/evt-web.html web/
# rename 
mv web/*.html web/index.html
# remove git info
rm -rf web/.git*
# build and run
docker build -t my-web-server-image .
docker run -p 4443:4443 my-web-server-image
# evt-challenges

Repo for Enterprise Vison Technologies (EVT) interview challenge.

## Notes 

First, this setup uses `http.server`, an easy to use Python package for launching web servers. I chose this because I can get a web-server up and running with a few lines of code.

Second, Because we are only displaying a single web page, only HTTP REST `GET` requests are supported on our URI.

Third, configuration is done using the file `webserver-config.py`. This file can be used to specify the hostname and port, as well as change certificates.

Fourth, I wrapped everything in a docker container to allow users to `git clone` to repo and run `./run.sh`. This program will build a docker container and set up the environment to listen on a specific container port (also forwarding the localhost's port). This, in theory, allows users to open their browsers to `https://localhost:4443` to view the webpage.

Lastly, the docker build command was tested on Mac and Linux (let me know if there are any issues).


## Web Server

This challenge required me to host a web-server to serve a provided index.html file.
This server must listen on a secure port using a self-signed certificate.


### Generating a certificate

For demoing purposes, a certificate is provided in the `server/` directory.
To generate your own certificate, you can type:

```
$ openssl req -new -x509 -keyout localhost.pem -out localhost.pem -days 365 -nodes
```

This certificate must be placed within the `server/` if generating your own.

### Specifying a host/port

By default, this program runs on `localhost` and listens on port `4443`.
You can change this within the dockerfile on the `CMD` line as appropriate.
The program automatically detects the newly-assigned port.

## Running

This repository contains a dockerfile to easily build and run this application.
For added convenience, a shell script is provided to run the docker commands.
To run the shell script, type:

```
$ chmod 777 run.sh
$ ./run.sh
```

This will start the webserver which will listen on port 4443.
You can visit `https://localhost:4443` to view the webpage.

Because the certificate is self-signed, you will get a warning!

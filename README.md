# evt-challenges

Repo for Enterprise Vison Technologies (EVT) interview challenge.

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
To run the program, type:

```
$ docker build -t my-web-server-image .
```

This will start the webserver which will listen on the provided port.
You can visit `https://localhost:{PORT}` to view the webpage.

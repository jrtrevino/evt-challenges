import http.server
import ssl
import argparse

# directory containing index.html file
DIRECTORY = "web"

# Manages GET requests on index.html
# Uses the SimpleHTTPRequestHandler and the defined directory above
# to manage the default directory.


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)


# Uses http server to serve the index.html file on host:port.
def serve(host, port):
    server_address = (host, port)
    # creates our HTTP server
    httpd = http.server.HTTPServer(server_address, Handler)
    # creates an SSL socketcontext with TLS protocol
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('./server/localhost.pem')
    # provide ssl socket to web server
    httpd.socket = context.wrap_socket(httpd.socket,
                                   server_side=True,)
    print(f"Server {host} running on port: {port}")
    # run our server!
    httpd.serve_forever()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('port', type=int, help="Port to run server on")
    parser.add_argument('host', type=str, help="host name")
    args = parser.parse_args()
    serve(args.host, args.port)

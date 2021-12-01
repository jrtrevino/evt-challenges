import http.server, ssl
import argparse
# directory containing index.html file
DIRECTORY = "web"


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)


# Uses http server to serve index.html file on host:port
def serve(host, port):
    server_address = (host, port)
    httpd = http.server.HTTPServer(server_address, Handler)
    httpd.socket = ssl.wrap_socket(httpd.socket,
                                server_side=True,
                                certfile='./server/localhost.pem',
                                ssl_version=ssl.PROTOCOL_TLS)
    print(f"Server {host} running on port: {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('port', type=int, help="Port to run server on") 
    parser.add_argument('host', type=str, help="host name") 
    args = parser.parse_args()
    serve(args.host, args.port)
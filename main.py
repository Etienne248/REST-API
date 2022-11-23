#Create a web server 
#Handle get and post on the web server 

import json
import argparse
from http.server import HTTPServer, BaseHTTPRequestHandler

COUNTER = 0

class S(BaseHTTPRequestHandler):
    def _set_headers(self, error_code : int):
        self.send_response(error_code)
        self.send_header("Content-type", "text/json")
        self.end_headers()

    def _html(self, message):
        """This just generates an HTML document that includes `message`
        in the body. Override, or re-write this do do more interesting stuff.
        """
        content = f"<html><body><h1>{message}</h1></body></html>\n"
        return content.encode("utf8")  # NOTE: must return a bytes object!

    def _json(self, obj : dict):
        return json.dumps(obj).encode("utf8")

    def do_GET(self):
        if self.path != "/counter":
            self._set_headers(404)
            return        
        self._set_headers(200)
        self.wfile.write(self._json({"counter":COUNTER}))

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        global COUNTER
        if self.path != "/counter/increment":
            self._set_headers(404)
            return
        COUNTER += 1
        self._set_headers(200)

def run(server_class=HTTPServer, handler_class=S, addr="localhost", port=8000):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)

    print(f"Starting httpd server on {addr}:{port}")
    httpd.serve_forever()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Run a simple HTTP server")
    parser.add_argument(
        "-l",
        "--listen",
        default="localhost",
        help="Specify the IP address on which the server listens",
    )
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=8000,
        help="Specify the port on which the server listens",
    )
    args = parser.parse_args()
    run(addr=args.listen, port=args.port)
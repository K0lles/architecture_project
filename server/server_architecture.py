from socketserver import ThreadingMixIn
from socketserver import TCPServer, BaseRequestHandler

from parsers.parsers import BaseRequestParser


class WebServer(BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024).strip()

        parsed_request = BaseRequestParser(data).parse_request()

        print(f'parsed_request: {parsed_request}')

        # there should be middleware call

        # Send HTTP response
        self.request.sendall('HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<html><body><h1>Hello, world!</h1></body></html>'.encode('utf-8'))


class ThreadedTCPServer(ThreadingMixIn, TCPServer):
    pass

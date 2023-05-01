from socketserver import ThreadingMixIn
from socketserver import TCPServer, BaseRequestHandler

from parsers.parsers import BaseRequestParser

from config.config import resolver


class WebServer(BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024).strip()

        parsed_request = BaseRequestParser(data).parse_request()

        view_class, kwargs = resolver.resolve(parsed_request['path'])
        header = b'HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n'
        answer = view_class(parsed_request, **kwargs).dispatch()

        response = header + answer

        self.request.sendall(response)

        # there should be middleware call

        # Send HTTP response
        # self.request.sendall('HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<html><body><h1>Hello, world!</h1></body></html>'.encode('utf-8'))


class ThreadedTCPServer(ThreadingMixIn, TCPServer):
    pass

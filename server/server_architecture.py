import json
from socketserver import ThreadingMixIn
from socketserver import TCPServer, BaseRequestHandler

from parsers.parsers import BaseRequestParser

from config.config import resolver


class WebServer(BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024).strip()

        parsed_request = BaseRequestParser(data).parse_request()

        header = b'HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n'
        try:
            view_class, kwargs = resolver.resolve(parsed_request['path'])
            answer = view_class(parsed_request, **kwargs).dispatch()

            response = header + answer

            self.request.sendall(response)
        except ValueError:
            answer = json.dumps({'error': 'Path does not exist'}).encode('utf-8')
            self.request.sendall(header + answer)


class ThreadedTCPServer(ThreadingMixIn, TCPServer):
    pass

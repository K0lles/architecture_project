import json

from validators.validators import ReceiptValidator


class HttpResponseNotAllowed:
    def __init__(self, allowed_methods):
        self.allowed_methods = allowed_methods

    def __call__(self, environ, start_response):
        status = "405 Method Not Allowed"
        headers = [("Content-type", "text/plain"), ("Allow", ", ".join(self.allowed_methods))]
        start_response(status, headers)
        return [b"Method not allowed"]


class View:
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']

    def __init__(self, request, *args, **kwargs):
        self.request = request
        self.args = args
        self.kwargs = kwargs

    def dispatch(self):
        handler = getattr(self, self.request['method'].lower(), self.http_method_not_allowed)
        return handler()

    def get(self):
        user_dict = {'name': 'dinesh', 'code': 'dr-01'}
        user_dict.update(self.kwargs)
        user_encode_data = json.dumps(user_dict).encode('utf-8')
        return user_encode_data

    def http_method_not_allowed(self):
        allowed_methods = [m.upper() for m in self.http_method_names if hasattr(self, m)]
        response = HttpResponseNotAllowed(allowed_methods)
        return response


class ReceiptView(View):

    def get(self):
        dct = json.dumps(self.request['body'].dict()).encode('utf-8')
        return dct

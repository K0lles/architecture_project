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

    def __init__(self, request):
        self.request = request
        self.args = []
        self.kwargs = {}

    def dispatch(self):
        handler = getattr(self, self.request.method.lower(), self.http_method_not_allowed)
        return handler()

    def http_method_not_allowed(self):
        allowed_methods = [m.upper() for m in self.http_method_names if hasattr(self, m)]
        response = HttpResponseNotAllowed(allowed_methods)
        return response

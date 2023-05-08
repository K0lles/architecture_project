from url_resolvers.url_resolvers import PathResolver
from view.base_views import View, ReceiptView


resolver = PathResolver()

resolver.add_url_pattern('/path/<int:someone>/', View)
resolver.add_url_pattern('/receipt/', ReceiptView)

from url_resolvers.url_resolvers import PathResolver
from view.base_views import View

resolver = PathResolver()

resolver.add_url_pattern('/path/<int:someone>/', View)

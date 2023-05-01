import re
from typing import Tuple, Any, Dict

from url_resolvers.base_resolvers import BasePathResolver


class PathResolver(BasePathResolver):

    def __init__(self):
        self.url_patterns = []

    def add_url_pattern(self, pattern: str, view_class: type):
        self.url_patterns.append((pattern, view_class))

    def resolve(self, path: str) -> Tuple[Any, Dict[str, Any]]:
        for pattern, view_class in self.url_patterns:
            regex_pattern = re.sub('<(\w+):', '<', pattern)
            regex_pattern = re.sub('<(\w+)>', r'(?P<\1>[^/]+)', regex_pattern)
            match = re.match(regex_pattern + '$', path)
            if match:
                kwargs = match.groupdict()
                return view_class, kwargs
        raise ValueError(f"No URL pattern found for path '{path}'")

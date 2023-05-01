from abc import ABC, abstractmethod
from typing import Tuple, Any


class BasePathResolver(ABC):

    @abstractmethod
    def add_url_pattern(self, pattern: str, view_class: type):
        """
        Make functionality for addition a URL pattern and its associated view class to the resolver.
        """
        ...

    @abstractmethod
    def resolve(self, path: str) -> Tuple[Any, Tuple[bytes | Any]]:
        """
        Make functionality for giving a path, returning the associated view class and any captured path
        segments as a tuple.
        """
        ...

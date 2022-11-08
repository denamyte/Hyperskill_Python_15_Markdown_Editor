from abc import ABC, abstractmethod
from typing import List


class MDBase(ABC):
    @abstractmethod
    def render(self) -> str:
        ...


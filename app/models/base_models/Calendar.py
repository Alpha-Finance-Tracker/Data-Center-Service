from abc import ABC, abstractmethod


class Calendar(ABC):
    @abstractmethod
    def interval(self):
        pass

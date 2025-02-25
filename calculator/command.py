from abc import ABC, abstractmethod

class Command(ABC):
    """Abstract base class for calculator commands."""
    @abstractmethod
    def execute(self):
        pass


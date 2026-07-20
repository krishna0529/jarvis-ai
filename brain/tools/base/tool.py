from abc import ABC, abstractmethod

class BaseTool(ABC):

    name = ""
    description = ""
    intents = []

    @abstractmethod
    def execute(self, entities: dict):
        pass
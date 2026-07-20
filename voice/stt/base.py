from abc import ABC, abstractmethod

class BaseSpeechEngine(ABC):

    @abstractmethod
    def transcribe(self, audio):

        pass
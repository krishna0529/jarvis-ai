# pyrefly: ignore [missing-import]
import sounddevice as sd

class AudioDevice:

    @staticmethod
    def list_devices():

        devices = sd.query_devices()

        return devices

    @staticmethod
    def default_input():

        return sd.default.device[0]

    @staticmethod
    def default_output():

        return sd.default.device[1]
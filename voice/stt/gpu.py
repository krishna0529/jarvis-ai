# pyrefly: ignore [missing-import]
import torch

class DeviceManager:

    @staticmethod
    def get():

        if torch.cuda.is_available():

            return "cuda"

        return "cpu"
from .Btn import Btn

class btnPickLocation(Btn):
    def __init__(self, input, x, y, width, height, isAvailable=True):
        super().__init__(input, x, y, width, height, isAvailable)
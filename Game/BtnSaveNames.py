from .PickLocation import PickLocation
from .frontend.Btn import Btn


class BtnSaveNames(Btn):
    def __init__(self, input, x, y, width, height, isAvailable=True):
        super().__init__(input, x, y, width, height, isAvailable)

    def onClick(self, window, names):
        pickLocation = PickLocation(window, names)
        pickLocation.render()
        return pickLocation.getPickList()

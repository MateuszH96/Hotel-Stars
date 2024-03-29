from .PickName import PickName
from .frontend.Btn import Btn


class BtnPickNumPlayer(Btn):
    def __init__(self, input, x, y, width, height, isAvailable=True):
        super().__init__(input, x, y, width, height, isAvailable)

    def onClick(self, numPlayer, window):
        pickName = PickName(numPlayer, window)
        pickName.render()
        return pickName.getResults()

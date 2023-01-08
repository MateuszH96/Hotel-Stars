# klasa nadrzędna do tworzenia przycisków
import pygame as pg

from . import GameObjects as GO
from . import ValuesFrontend as VF


class Btn(GO.GameObject):
    # nadrzędna klasa tworzenia przycisków
    def __init__(self, input, x, y, width, height, isAvailable=True):
        super().__init__(x, y, width, height, isAvailable)
        self.setImage(input)

    def setImage(self, input):
        self.__image = pg.image.load(VF.IMG_PATH + input)
        self.__image = pg.transform.scale(
            self.__image, (self._width, self._height))

    def getImage(self):
        return self.__image

    def onClick(self):
        pass

from .GameObjects import GameObject
from . import ValuesFrontend as VF
import pygame as pg
class Img(GameObject):
    def __init__(self,image, x, y, width, height, isAvailable=True):
        super().__init__(x, y, width, height, isAvailable)
        self.setImage(image)
        
    def setImage(self, input):
        self.__image = pg.image.load(VF.IMG_PATH + input)
        self.__image = pg.transform.scale(
            self.__image, (self._width, self._height))

    def getImage(self):
        return self.__image
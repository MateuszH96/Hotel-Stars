# klasa nadrzędna do tworzenia przycisków
import pygame as pg

from .Img import Img
from . import ValuesFrontend as VF


class Btn(Img):
    # nadrzędna klasa tworzenia przycisków
    def __init__(self, image, x=0, y=0, width=0, height=0, isAvailable=True):
        super().__init__(image, x, y, width, height, isAvailable)

    def onClick(self):
        pass

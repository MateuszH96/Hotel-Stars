import pygame as pg
from Game.NumOfPLayers import *
from Game.frontend.ValuesFrontend import MUL, WIDTH, HEIGHT
pg.init()
SIZE=(WIDTH,HEIGHT)
SCREEN = pg.display.set_mode(SIZE)
CLOCK = pg.time.Clock()
game = NumOfPlayer(SCREEN,CLOCK)
game.render()
from . import Btn
import pygame as pg
class Collision:
    @staticmethod
    def isCollisionRectMouse(button):
        mousePos = pg.mouse.get_pos()
        mouseX = mousePos[0]+int(button.getWidth()/2)
        mouseY = mousePos[1]+int(button.getHeight()/2)
        x = mouseX>=button.getX() and mouseX<=(button.getX() + button.getWidth())
        y = mouseY>=button.getY() and mouseY<=(button.getY() + button.getHeight())
        return (x and y)
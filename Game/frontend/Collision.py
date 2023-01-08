import pygame as pg

from . import Btn


class Collision:
    @staticmethod
    def isCollisionRectMouse(objectToCollision):
        # wykrywanie kolizji kliknięcia na objekt
        mousePos = pg.mouse.get_pos()
        mouseX = mousePos[0]+int(objectToCollision.getWidth()/2)
        mouseY = mousePos[1]+int(objectToCollision.getHeight()/2)
        x = mouseX >= objectToCollision.getX() and mouseX <= (
            objectToCollision.getX() + objectToCollision.getWidth())
        y = mouseY >= objectToCollision.getY() and mouseY <= (
            objectToCollision.getY() + objectToCollision.getHeight())
        return (x and y)

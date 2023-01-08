import pygame as pg

from . import ValueGame as VG
from .frontend.Btn import Btn
from .frontend.btnPickLocation import btnPickLocation
from .frontend.Collision import Collision
from .frontend.Draw import Draw
from .frontend.Window import Window


class PickLocation:
    def __init__(self, window: Window, names):
        self.__window = window
        self.__names = names
        self.__player = 0
        self.__font = pg.font.SysFont(
            VG.FONT_NAME_LOCATION, VG.FONT_SIZE_LOCATION)
        self.__createObjects()
        self.__isPickedLocation = False
        self.__pickedPosition = 0
        self.__pickList = []

    def getPickList(self):
        # zwracanie listy wyborów lokalizacji graczy
        return self.__pickList

    def render(self):
        # generowanie obrazu i logiki wyboru lokalizacji gracza
        pg.init()
        pg.display.set_caption(VG.GAME_NAME)
        while self.__player < len(self.__names):
            self.__window.getScreen().blit(self.__locationToChoose, (0, 0))
            listToDraw = Draw.transfomrToCenter(self.__createListObject())
            for i in listToDraw:
                self.__window.getScreen().blit(i[0], i[1])
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                if event.type == pg.MOUSEBUTTONDOWN and self.__isPickedLocation and Collision.isCollisionRectMouse(self.__pickLocation):
                    self.__pickList.append(self.__pickedPosition)
                    self.__pickedPosition = 0
                    self.__player += 1
                    self.__isPickedLocation = False
                elif event.type == pg.MOUSEBUTTONDOWN:
                    mouseX = pg.mouse.get_pos()[0]
                    self.__pickedPosition = int(mouseX/VG.WIDTH_RECTANGLE_PICK)
                    self.__isPickedLocation = True
            self.__createRectangleBorder()
            pg.display.flip()
            self.__window.getClock().tick(60)

    def __createObjects(self):
        self.__locationToChoose = pg.image.load(VG.VG_IMG_PATH+"Location.jpg")
        self.__locationToChoose = pg.transform.scale(
            self.__locationToChoose, (VG.SIZE))
        self.__staticText = self.__font.render(
            "Teraz wybiera", True, VG.FONT_COLOR_LOCATION)
        self.__pickLocation = Btn(
            "OK.jpg", VG.OK_COORDINATE_X, VG.OK_COORDINATE_Y, VG.OK_WIDTH, VG.OK_HEIGHT)

    def __createListObject(self):
        dynamicText = self.__font.render(
            self.__names[self.__player], True, VG.FONT_COLOR_LOCATION)
        dynamicTextPosition = (VG.DYNAMIC_TEXT_COORDINATE_X,
                               VG.DYNAMIC_TEXT_COORDINATE_Y)
        listOfObjects = []
        staticTextCoordinates = (
            VG.STATIC_TEXT_COORDINATE_X, VG.STATIC_TEXT_COORDINATE_Y)
        listOfObjects.append([self.__staticText, staticTextCoordinates])
        listOfObjects.append([self.__pickLocation.getImage(
        ), (self.__pickLocation.getX(), self.__pickLocation.getY())])
        listOfObjects.append([dynamicText, dynamicTextPosition])
        return listOfObjects

    def __createRectangleBorder(self):
        mouseX = pg.mouse.get_pos()[0]
        pos = int(mouseX/VG.WIDTH_RECTANGLE_PICK)
        xRect = VG.WIDTH_RECTANGLE_PICK*pos
        widthRect = VG.WIDTH_RECTANGLE_PICK
        pg.draw.rect(self.__window.getScreen(), (255, 0, 0),
                     (xRect, 0, widthRect, VG.HEIGHT), VG.BORDER_RECT_TO_PICK)
        if self.__isPickedLocation:
            xRect = VG.WIDTH_RECTANGLE_PICK*self.__pickedPosition
            widthRect = VG.WIDTH_RECTANGLE_PICK
            pg.draw.rect(self.__window.getScreen(), (0, 255, 0),
                         (xRect, 0, widthRect, VG.HEIGHT), VG.BORDER_RECT_PICKED)

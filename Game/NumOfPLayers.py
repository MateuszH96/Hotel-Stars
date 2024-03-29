import pygame as pg

from . import ValueGame as VG
from .frontend.Btn import Btn
from .BtnPickNumPlayer import BtnPickNumPlayer
from .frontend.Collision import Collision
from .frontend.Draw import Draw
from .frontend.Window import Window
from .backend.Player import Player
from .GameHotel import GameHotel
from .frontend.Img import Img

class NumOfPlayer:
    def __init__(self, screen, clock):
        self.__window = Window(clock, screen)
        self.__players = 2
        self.__font = pg.font.SysFont(
            VG.FONT_NAME_NUM_PLAYER, VG.FONT_SIZE_NUM_PLAYER)
        self.__createObjects()
        pass

    def render(self):
        # generownie obrazu i logi okna wyboru graczy
        pg.init()
        pg.display.set_caption(VG.GAME_NAME)
        repeat = True
        while repeat:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    repeat = not repeat
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.__changePlayersValue()
                    self.__isOkClicked()
            self.__window.getScreen().fill(VG.COLOR_FILL_WINDOW)
            self.__window.getScreen().blit(self.__background, (0, 0))
            listToDraw = Draw.transfomrToCenter(self.__createListObjects())
            for i in listToDraw:
                self.__window.getScreen().blit(i[0], i[1])
            pg.display.flip()
            self.__window.getClock().tick(60)
        pg.quit()

    def __isOkClicked(self):
        if Collision.isCollisionRectMouse(self.__btnOK):
            startValues = self.__btnOK.onClick(self.__players, self.__window)
            game = GameHotel(self.__window, self.__createListPlayers(startValues[0],startValues[1]))
            game.game()

    def __createListObjects(self):
        text = self.__font.render(
            str(self.__players), True, VG.FONT_COLOR_NUM_PLAYER)
        toReturn = []
        numOfPlayerTxT = Img('NumberOfPlayers.png', VG.WIDTH/2, VG.HEIGHT/4, 600,150)
        toReturn.append([numOfPlayerTxT.getImage(),(numOfPlayerTxT.getX(),numOfPlayerTxT.getY())])
        leftArrowCoordinates = (
            self.__btnLeftArrow.getX(), self.__btnLeftArrow.getY())
        toReturn.append([self.__btnLeftArrow.getImage(), leftArrowCoordinates])
        rightArrowCoordinates = (
            self.__btnRightArrow.getX(), self.__btnRightArrow.getY())
        toReturn.append(
            [self.__btnRightArrow.getImage(), rightArrowCoordinates])
        okCoordinates = (self.__btnOK.getX(), self.__btnOK.getY())
        toReturn.append([self.__btnOK.getImage(), okCoordinates])
        toReturn.append([text, VG.TEXT_COORDINATE])
        return toReturn

    def __createObjects(self):
        self.__btnLeftArrow = Btn(
            'LeftArrow.png', VG.LEFT_ARROW_COORDINATE_X, VG.LEFT_ARROW_COORDINATE_Y, 100, 100)
        self.__btnRightArrow = Btn(
            'RightArrow.png', VG.RIGHT_ARROW_COORDINATE_X, VG.LEFT_ARROW_COORDINATE_Y, 100, 100)
        self.__btnOK = BtnPickNumPlayer(
            'OK.png', VG.OK_COORDINATE_X, VG.OK_COORDINATE_X, 200, 100)
        self.__background = pg.image.load(VG.VG_IMG_PATH+"Background.png")
        self.__background = pg.transform.scale(self.__background, (VG.SIZE))

    def __collision(self):
        if Collision.isCollisionRectMouse(self.__btnLeftArrow):
            return VG.LEFT_ARROW_PRESSED
        if Collision.isCollisionRectMouse(self.__btnRightArrow):
            return VG.RIGHT_ARROW_PRESSED
        return VG.NOT_PRESSED

    def __changePlayersValue(self):
        tmp1 = VG.CHANGE_VALUE_PLAYERS[self.__collision()]
        tmp = self.__players + tmp1
        if tmp >= 2 and tmp <= 8:
            self.__players = tmp

    def __createListPlayers(self, name, location):
        toReturn = []

        for i, j in zip(name, location):
            toReturn.append(Player(i, j))

        return toReturn

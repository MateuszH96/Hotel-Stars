from .frontend.Window import Window
from .frontend.Img import Img
from . import ValueGame as VG
from .frontend.Draw import Draw
from .backend.Player import Player
from .backend.Hotel import Hotel
from .backend.Room import Room
from .frontend.Btn import Btn
from .frontend.Collision import Collision
from .BtnNextFloor import BtnNextFloor
from .BtnPrevFloor import BtnPrevFloor
from .BtnAddFloor import BtnAddFloor
from .BtnBuyRoom import BtnBuyRoom
from .BtnBank import BtnBank
from .BtnPassTurn import BtnPassTurn
from .BtnPassRound import BtnPassRound
from .BtnDowngradeRoom import BtnDowngradeRoom
from .BtnUpgradeRoom import BtnUpgradeRoom
import pygame as pg
import math
# TODO:
# __roomListShow służy do wyświetlania, potrzebuję jeszcze listę przycisków pokojów


class GameHotel:
    def __init__(self, window, players: Player):
        self.__window = window
        self.__font = pg.font.SysFont(
            VG.GAME_FONT_NAME, VG.GAME_FONT_SIZE, bold=True)
        self.__playerNum = 0
        self.__players = players
        self.__isRectangleBorderDraw = False
        self.__rectangleBorder = [0, 0, 0, 0]
        self.__floorToChange = 0
        self.__rooomToChange = 0
        self.__createStaticObjects()

    def __createStaticObjects(self):
        self.__background = Img("BackgroundHotel.png", VG.BACKGROUND_GAME_X,
                                VG.BACKGROUND_GAME_Y, VG.WIDTH_GAME_BACKGROUND, VG.HEIGHT_GAME_BACKGROUND)
        self.__menuBar = Img("MenuBarBackground.png", VG.BACKGROUND_MENUBAR_X,
                             VG.BACKGROUND_MENUBAR_Y, VG.WIDTH_MENUBAR_BACKGROUND, VG.HEIGHT_MENUBAR_BACKGROUND)

    def __createStatlicObjectList(self):
        staticObjectList = []
        staticObjectList.append([self.__background.getImage(
        ), (self.__background.getX(), self.__background.getY())])
        staticObjectList.append([self.__menuBar.getImage(
        ), (self.__menuBar.getX(), self.__menuBar.getY())])  # TODO
        self.__name = self.__font.render(
            self.__players[self.__playerNum].getName(), True, VG.GAME_FONT_COLOR)
        self.__money = self.__font.render(
            str(self.__players[self.__playerNum].getMoney()), True, VG.GAME_FONT_COLOR)
        return staticObjectList

    def __createDynamicObjectList(self):
        self.__name = self.__font.render(
            self.__players[self.__playerNum].getName(), True, VG.GAME_FONT_COLOR)
        self.__money = self.__font.render("$" +
                                          str(self.__players[self.__playerNum].getMoney()), True, VG.GAME_FONT_COLOR)
        self.__createRoomList()
        toReturn = self.__roomListShow
        self.__createMenubarList()
        toReturn += self.__menuBarList
        roomLevel = self.__font.render(
            str(self.__players[self.__playerNum].getFloorNum()+1), True, VG.GAME_FONT_COLOR)
        toReturn.append([roomLevel, VG.FLOOR_TEXT_COORDINATE])
        return toReturn

    def __createRoomList(self):
        listRoom = self.__players[self.__playerNum].getHotel().getFloor(
            self.__players[self.__playerNum].getFloorNum())
        upLineRoom = 0
        downLineRoom = 0
        self.__roomList = []
        self.__roomListShow = []
        for i in range(len(listRoom)):
            imgName = "RoomLevel" + str(listRoom[i].getRoomLevel()) + ".png"
            if i < VG.NEXT_LINE_ROOM:
                y = VG.UP_ROOM_Y
                x = int(upLineRoom*VG.WIDTH_ROOM+VG.WIDTH_ROOM/2)
                upLineRoom += 1
            else:
                y = VG.DOWN_ROOM_Y
                x = int(downLineRoom*VG.WIDTH_ROOM+VG.WIDTH_ROOM/2)
                downLineRoom += 1
            tmp = Btn(imgName, x, y, VG.WIDTH_ROOM, VG.HEIGHT_ROOM)
            self.__roomList.append(tmp)
            self.__roomListShow.append([tmp.getImage(), (x, y)])

    def __createMenubarList(self):
        self.__menuBarList = []
        btnPrevFloor = BtnPrevFloor("LeftArrow.png", VG.PREV_FLOOR_X,
                                    VG.PREV_FLOOR_Y, VG.PREV_FLOOR_WIDTH, VG.PREV_FLOOR_HEIGHT)
        self.__menuBarList.append(
            [btnPrevFloor.getImage(), (btnPrevFloor.getX(), btnPrevFloor.getY())])
        btnNextFloor = BtnNextFloor("RightArrow.png", VG.NEXT_FLOOR_X,
                                    VG.NEXT_FLOOR_Y, VG.NEXT_FLOOR_WIDTH, VG.NEXT_FLOOR_HEIGHT)
        self.__menuBarList.append(Draw.getImgValuesToCenter(btnNextFloor))
        btnAddFloor = BtnAddFloor("AddFloor.png", VG.ADD_FLOOR_X,
                                  VG.ADD_FLOOR_Y, VG.ADD_FLOOR_WIDTH, VG.ADD_FLOOR_HEIGHT)
        self.__menuBarList.append(Draw.getImgValuesToCenter(btnAddFloor))

        btnBuyRoom = BtnBuyRoom("BuyRoom.png", VG.BUY_ROOM_X,
                                VG.BUY_ROOM_Y, VG.BUY_ROOM_WIDTH, VG.BUY_ROOM_HEIGHT)
        self.__menuBarList.append(Draw.getImgValuesToCenter(btnBuyRoom))

        btnUpgradeRoom = BtnUpgradeRoom("UpgradeRoom.png", VG.UPGRADE_ROOM_X,
                                        VG.UPGRADE_ROOM_Y, VG.UPGRADE_ROOM_WIDTH, VG.UPGRADE_ROOM_HEIGHT)
        self.__menuBarList.append(Draw.getImgValuesToCenter(btnUpgradeRoom))

        btnDowngradeRoom = BtnDowngradeRoom("DowngradeRoom.png", VG.DOWNGRADE_ROOM_X,
                                            VG.DOWNGRADE_ROOM_Y, VG.DOWNGRADE_ROOM_WIDTH, VG.DOWNGRADE_ROOM_HEIGHT)
        self.__menuBarList.append(Draw.getImgValuesToCenter(btnDowngradeRoom))

        btnBank = BtnBank("Bank.png", VG.SWITCH_TO_BANK_X, VG.SWITCH_TO_BANK_Y,
                          VG.SWITCH_TO_BANK_WIDTH, VG.SWITCH_TO_BANK_HEIGHT)
        self.__menuBarList.append(Draw.getImgValuesToCenter(btnBank))

        btnPassTurn = BtnPassTurn("Decline.png", VG.BTN_PASS_TURN__X, VG.BTN_PASS_TURN__Y,
                                  VG.BTN_PASS_TURN__WIDTH, VG.BTN_PASS_TURN__HEIGHT)
        self.__menuBarList.append(Draw.getImgValuesToCenter(btnPassTurn))
        btnPassRound = BtnPassRound("Pass.png", VG.BTN_PASS_ROUND__X, VG.BTN_PASS_ROUND__Y,
                                    VG.BTN_PASS_ROUND__WIDTH, VG.BTN_PASS_ROUND__HEIGHT)
        self.__menuBarList.append(Draw.getImgValuesToCenter(btnPassRound))
        self.__menuBarListToColl = [btnPrevFloor, btnNextFloor, btnAddFloor,
                                    btnBuyRoom, btnUpgradeRoom, btnDowngradeRoom, btnBank, btnPassTurn, btnPassRound]

    def game(self):
        for i in range(16):
            pg.display.set_caption(VG.GAME_NAME+" Runda: "+str(i+1))
            repeatEveryPlayer = True
            for j in self.__players:
                j.setPassRound(False)
                j.nextRound()
            while repeatEveryPlayer:
                for j in self.__players:
                    j.setPassTurn(False)
                for j in range(len(self.__players)):
                    self.__playerNum = j
                    if not self.__players[self.__playerNum].getPassRound():
                        repeat = True
                        staticObjects = self.__createStatlicObjectList()
                        while repeat:
                            if self.__players[self.__playerNum].getPassRound() or self.__players[self.__playerNum].getPassTurn():
                                repeat = False
                            Draw.draw(staticObjects+[[self.__name, VG.GAME_NAME_COORDINATE], [
                                self.__money, VG.GAME_MONEY_COORDINATE]], window=self.__window.getScreen())
                            listDynamicObjects = self.__createDynamicObjectList()
                            listDynamicObjects = Draw.transfomrToCenter(
                                listDynamicObjects)
                            Draw.draw(listDynamicObjects,
                                      window=self.__window.getScreen())
                            if self.__isRectangleBorderDraw:
                                pg.draw.rect(self.__window.getScreen(
                                ), (0, 255, 0), self.__rectangleBorder, 4)
                                pass
                            for event in pg.event.get():
                                if event.type == pg.QUIT:
                                    pg.quit()
                                    exit()
                                if event.type == pg.MOUSEBUTTONDOWN:
                                    self.__btnPressed()
                                pg.display.update()
                                self.__window.getClock().tick(60)
                count = 0
                for j in self.__players:
                    if j.getPassRound():
                        count += 1
                if count == len(self.__players):
                    self.__makeCalc()
                    repeatEveryPlayer = False

    def __btnPressed(self):

        if Collision.isCollisionRectMouse(self.__menuBar, False):
            self.__menubarPressed()
        else:
            self.__roomListShowPressed()
        return

    def __menubarPressed(self):
        for i in self.__menuBarListToColl:
            if Collision.isCollisionRectMouse(i):
                if not (isinstance(i, BtnDowngradeRoom) or isinstance(i, BtnUpgradeRoom)):
                    i.onClick(self.__players[self.__playerNum])
                    self.__isRectangleBorderDraw = False
                else:
                    i.onClick(self.__players[self.__playerNum],
                              self.__floorToChange, self.__rooomToChange)
        return

    def __roomListShowPressed(self):
        for i in range(len(self.__roomList)):
            if Collision.isCollisionRectMouse(self.__roomList[i]):
                self.__isRectangleBorderDraw = True
                self.__rectangleBorder = [self.__roomList[i].getX()-self.__roomList[i].getWidth()/2, self.__roomList[i].getY(
                )-self.__roomList[i].getHeight()/2, self.__roomList[i].getWidth(), self.__roomList[i].getHeight()]
                self.__floorToChange = self.__players[self.__playerNum].getFloorNum(
                )
                tmpOffset = 0
                if self.__roomList[i].getY() > VG.HEIGHT/2:
                    tmpOffset = 5
                self.__rooomToChange = tmpOffset + \
                    int(self.__roomList[i].getX() /
                        self.__roomList[i].getWidth())
        return

    def __makeCalc(self):
        for i in self.__players:
            i.CalcEndRound()
        pass

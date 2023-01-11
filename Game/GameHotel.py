from .frontend.Window import Window
from .frontend.Img import Img
from . import ValueGame as VG
from .frontend.Draw import Draw
from .backend.Player import Player
from .backend.Hotel import Hotel
from .backend.Room import Room
from .frontend.Btn import Btn
from .frontend.Collision import Collision
import pygame as pg
#TODO:
#__roomListShow służy do wyświetlania, potrzebuję jeszcze listę przycisków pokojów

class GameHotel:
    def __init__(self, window, players: Player):
        self.__window = window
        self.__font = pg.font.SysFont(VG.GAME_FONT_NAME, VG.GAME_FONT_SIZE, bold=True)
        self.__playerNum = 0
        self.__players = players
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
        staticObjectList.append(
            [self.__menuBar.getImage(), (self.__menuBar.getX(), self.__menuBar.getY())])
        self.__name = self.__font.render(
            self.__players[self.__playerNum].getName(), True,VG.GAME_FONT_COLOR)
        self.__money = self.__font.render(
            str(self.__players[self.__playerNum].getMoney()), True,VG.GAME_FONT_COLOR)
        return staticObjectList

    def __createDynamicObjectList(self):
        self.__name = self.__font.render(
            self.__players[self.__playerNum].getName(), True,VG.GAME_FONT_COLOR)
        self.__money = self.__font.render("$"+
            str(self.__players[self.__playerNum].getMoney()), True,VG.GAME_FONT_COLOR)
        self.__createRoomList()
        toReturn = self.__roomListShow
        self.__createMenubarList()
        toReturn += self.__menuBarList
        roomLevel = self.__font.render(str(self.__players[self.__playerNum].getFloorNum()+1),True, VG.GAME_FONT_COLOR)
        toReturn.append([roomLevel,VG.FLOOR_TEXT_COORDINATE])
        return toReturn
    
    def __createRoomList(self):
        listRoom = self.__players[self.__playerNum].getHotel().getFloor(self.__players[self.__playerNum].getFloorNum())
        upLineRoom =0
        downLineRoom = 0
        self.__roomList=[]
        self.__roomListShow =[]
        for i in range(len(listRoom)):
            imgName = "RoomLevel" + str(listRoom[i].getRoomLevel()) + ".png"
            if i < VG.NEXT_LINE_ROOM:
                y=VG.UP_ROOM_Y
                x=int(upLineRoom*VG.WIDTH_ROOM+VG.WIDTH_ROOM/2)
                upLineRoom +=1
            else:
                y=VG.DOWN_ROOM_Y
                x=int(downLineRoom*VG.WIDTH_ROOM+VG.WIDTH_ROOM/2)
                downLineRoom +=1
            tmp = Btn(imgName,x,y,VG.WIDTH_ROOM,VG.HEIGHT_ROOM)
            self.__roomList.append(tmp)
            self.__roomListShow.append([tmp.getImage(),(x,y)])
    
    def __createMenubarList(self):
        self.__menuBarList = []
        btnPrevFloor = Btn("LeftArrow.png",VG.PREV_FLOOR_X,VG.PREV_FLOOR_Y,VG.PREV_FLOOR_WIDTH,VG.PREV_FLOOR_HEIGHT)
        self.__menuBarList.append([btnPrevFloor.getImage(),(btnPrevFloor.getX(),btnPrevFloor.getY())])
        btnNextFloor = Btn("RightArrow.png",VG.NEXT_FLOOR_X,VG.NEXT_FLOOR_Y,VG.NEXT_FLOOR_WIDTH,VG.NEXT_FLOOR_HEIGHT)
        self.__menuBarList.append(Draw.getImgValuesToCenter(btnNextFloor))
        btnAddFloor = Btn("AddFloor.png",VG.ADD_FLOOR_X,VG.ADD_FLOOR_Y,VG.ADD_FLOOR_WIDTH,VG.ADD_FLOOR_HEIGHT)
        self.__menuBarList.append(Draw.getImgValuesToCenter(btnAddFloor))
        
        btnAddFloor = Btn("BuyRoom.png",VG.BUY_ROOM_X,VG.BUY_ROOM_Y,VG.BUY_ROOM_WIDTH,VG.BUY_ROOM_HEIGHT)
        self.__menuBarList.append(Draw.getImgValuesToCenter(btnAddFloor))
        
        btnAddFloor = Btn("UpgradeRoom.png",VG.UPGRADE_ROOM_X,VG.UPGRADE_ROOM_Y,VG.UPGRADE_ROOM_WIDTH,VG.UPGRADE_ROOM_HEIGHT)
        self.__menuBarList.append(Draw.getImgValuesToCenter(btnAddFloor))
        
        btnAddFloor = Btn("DowngradeRoom.png",VG.DOWNGRADE_ROOM_X,VG.DOWNGRADE_ROOM_Y,VG.DOWNGRADE_ROOM_WIDTH,VG.DOWNGRADE_ROOM_HEIGHT)
        self.__menuBarList.append(Draw.getImgValuesToCenter(btnAddFloor))
        
        btnAddFloor = Btn("Bank.png",VG.SWITCH_TO_BANK_X,VG.SWITCH_TO_BANK_Y,VG.SWITCH_TO_BANK_WIDTH,VG.SWITCH_TO_BANK_HEIGHT)
        self.__menuBarList.append(Draw.getImgValuesToCenter(btnAddFloor))
    def game(self):
        repeat = True
        staticObjects = self.__createStatlicObjectList()
        while repeat:
            Draw.draw(staticObjects+[[self.__name,VG.GAME_NAME_COORDINATE],[self.__money,VG.GAME_MONEY_COORDINATE]], window=self.__window.getScreen())
            listDynamicObjects = self.__createDynamicObjectList()
            listDynamicObjects = Draw.transfomrToCenter(listDynamicObjects)
            Draw.draw(listDynamicObjects, window=self.__window.getScreen())
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.__btnPressed()
            pg.display.update()
            self.__window.getClock().tick(60)
    def __btnPressed(self):
        if Collision.isCollisionRectMouse(self.__menuBar):
            self.__menubarPressed()
        else:
            self.__roomListShowPressed()
        print("--------")
        return
    
    def __menubarPressed(self):
        return
    
    def __roomListShowPressed(self):
        for i in range(len(self.__roomList)):
            if Collision.isCollisionRectMouse(self.__roomList[i]):
                print(f"Pokój nr{i+1}")
        return
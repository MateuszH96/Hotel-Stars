from .frontend.Img import Img
from .backend.Player import Player
from .frontend.Draw import Draw
from . import ValueGame as VG
from .frontend.Window import Window
from .frontend.Collision import Collision
from .frontend.Btn import Btn
import pygame as pg
import pygame_gui as pg_ui

class BankView:
    def __init__(self,player: Player):
        SIZE=(VG.WIDTH,VG.HEIGHT)
        self.__screen = pg.display.set_mode(SIZE)
        self.__clock = pg.time.Clock()    
        self.__font = pg.font.SysFont(VG.BANK_FONT_NAME,VG.BANK_FONT_SIZE,True)
        self.__player = player
        self.__manager = pg_ui.UIManager((VG.WIDTH,VG.HEIGHT))
        self.__createStaticOcjects()
        self.__createInputs()
    
    def __createInputs(self):
        self.__inputLvl1 = pg_ui.elements.UITextEntryLine(relative_rect=pg.Rect((VG.INPUT_ROOM_COST_X,VG.INPUT_ROOM1_COST_Y),(VG.INPUT_ROOM_COST_WIDTH,VG.INPUT_ROOM_COST_HEIGHT)),manager=self.__manager,object_id='#room_lvl1')
        self.__inputLvl1.set_text(str(self.__player.getHotel().getLevelRoomCost(1)))
        self.__inputLvl2 = pg_ui.elements.UITextEntryLine(relative_rect=pg.Rect((VG.INPUT_ROOM_COST_X,VG.INPUT_ROOM2_COST_Y),(VG.INPUT_ROOM_COST_WIDTH,VG.INPUT_ROOM_COST_HEIGHT)),manager=self.__manager,object_id='#room_lvl2')
        self.__inputLvl2.set_text(str(self.__player.getHotel().getLevelRoomCost(2)))
        self.__inputLvl3 = pg_ui.elements.UITextEntryLine(relative_rect=pg.Rect((VG.INPUT_ROOM_COST_X,VG.INPUT_ROOM3_COST_Y),(VG.INPUT_ROOM_COST_WIDTH,VG.INPUT_ROOM_COST_HEIGHT)),manager=self.__manager,object_id='#room_lvl3')
        self.__inputLvl3.set_text(str(self.__player.getHotel().getLevelRoomCost(3)))
        self.__inputLvl4 = pg_ui.elements.UITextEntryLine(relative_rect=pg.Rect((VG.INPUT_ROOM_COST_X,VG.INPUT_ROOM4_COST_Y),(VG.INPUT_ROOM_COST_WIDTH,VG.INPUT_ROOM_COST_HEIGHT)),manager=self.__manager,object_id='#room_lvl4')
        self.__inputLvl4.set_text(str(self.__player.getHotel().getLevelRoomCost(4)))
        if self.__player.getRound() >3:
            self.__inputLoan = pg_ui.elements.UITextEntryLine(relative_rect=pg.Rect((VG.LOAN_INPUT_X,VG.LOAN_INPUT_Y),(VG.LOAN_INPUT_WIDTH,VG.LOAN_INPUT_HEIGHT)),manager=self.__manager,object_id='#loan')
            tmp = self.__player.getBank().getCreditorthiness()
            if tmp<0:
                tmp = 0
            self.__inputLoan.set_text(str(tmp))
        pass
    
    
    def __createStaticOcjects(self):
        self.__txtList = []
        self.__background= Img("Background.png",VG.BANK_BACKGROUND_X,VG.BANK_BACKGROUND_Y,VG.BANK_BACKGROUND_WIDTH,VG.BANK_BACKGROUND_HEIGHT)
        lvl1Room = self.__font.render("Koszt wynajmu pokoju Poziomu 1", True, VG.BANK_FONT_COLOR)
        self.__txtList.append([lvl1Room,VG.ROOM1_LVL_COORDINATES])
        lvl2Room = self.__font.render("Koszt wynajmu pokoju Poziomu 2", True, VG.BANK_FONT_COLOR)
        self.__txtList.append([lvl2Room,VG.ROOM2_LVL_COORDINATES])
        lvl3Room = self.__font.render("Koszt wynajmu pokoju Poziomu 3", True, VG.BANK_FONT_COLOR)
        self.__txtList.append([lvl3Room,VG.ROOM3_LVL_COORDINATES])
        lvl4Room = self.__font.render("Koszt wynajmu pokoju Poziomu VIP", True, VG.BANK_FONT_COLOR)
        self.__txtList.append([lvl4Room,VG.ROOM4_LVL_COORDINATES])
        self.__btnOkRoomPrice = Btn("Ok.png",VG.BTN_PRICE_ROOM_X,VG.BTN_PRICE_ROOM_Y,VG.BTN_PRICE_ROOM_WIDTH,VG.BTN_PRICE_ROOM_HEIGHT)
        self.__txtList.append([self.__btnOkRoomPrice.getImage(),VG.BTN_PRICE_ROOM_COORDINATE])
        if self.__player.getRound() >3:
            textLoan =''
            if self.__player.getLoanStatus():
                textLoan = 'Zwróć Pożyczkę (10 rat)'
            else:
                textLoan = 'Wez Pożyczkę'
            loanText = self.__font.render(textLoan, True, VG.BANK_FONT_COLOR)
            self.__txtList.append([loanText,VG.LOAN_TEXT_COORDINATES])
    
    def render(self):
        repeat = True
        backgroundToDraw =Draw.transfomrToCenter([Draw.getImgValuesToCenter(self.__background)])
        Draw.draw(backgroundToDraw,self.__screen )
        Draw.draw(self.__txtList,self.__screen)
        UI_REFRESH_RATE = self.__clock.tick(60)/1000
        while repeat:
            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.MOUSEBUTTONDOWN and not Collision.isCollisionRectMouse(self.__background)):
                    repeat = False
                if event.type == pg.MOUSEBUTTONDOWN and Collision.isCollisionRectMouse(self.__btnOkRoomPrice):
                    self.__pressBtn()
                self.__manager.process_events(event) 
            self.__manager.update(UI_REFRESH_RATE)
            self.__manager.draw_ui(self.__screen)
            pg.display.update()
        
    def __pressBtn(self):
        if self.__inputLvl1.get_text().isdigit():
            self.__player.getHotel().setRoomLevelCost(1,int(self.__inputLvl1.get_text()))
        if self.__inputLvl2.get_text().isdigit():
            self.__player.getHotel().setRoomLevelCost(2,int(self.__inputLvl2.get_text()))
        if self.__inputLvl3.get_text().isdigit():
            self.__player.getHotel().setRoomLevelCost(3,int(self.__inputLvl3.get_text()))
        if self.__inputLvl4.get_text().isdigit():
            self.__player.getHotel().setRoomLevelCost(4,int(self.__inputLvl4.get_text()))
        pass
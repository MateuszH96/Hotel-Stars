import pygame as pg
import pygame_gui as pg_ui
from . import ValueGame as VG
from .frontend import ValuesFrontend as VF
from .frontend.Window import Window
from .frontend.InputText import InputText
from .frontend.CreateManagerInputs import CreateManagerInputs
from .frontend.BtnSaveNames import BtnSaveNames
from .frontend.Draw import Draw
class PickName:
    def __init__(self,numPlayer, window: Window):
        self.__numPlayer = numPlayer
        self.__window = window
        self.__btnSaveNames = BtnSaveNames("Start.jpg",VG.SAVE_NAME_COORDINATE_X,VG.SAVE_NAME_COORDINATE_Y,400,200)
        self.__inputsList = CreateManagerInputs.createInputsList(self.__numPlayer,VF.SIZE,"Podaj imię ","Gracz")
        self.__manager = CreateManagerInputs.createManagerInputs(self.__inputsList,VF.SIZE)
        self.__background = pg.image.load(VG.VG_IMG_PATH + "Background.jpg")
        self.__background = pg.transform.scale(self.__background,(VG.SIZE))
        
    def render(self):
        pg.init()
        pg.display.set_caption(VG.GAME_NAME)
        repeat = True
        btnPos = Draw.transfomrToCenter([[self.__btnSaveNames.getImage(),(self.__btnSaveNames.getX(),self.__btnSaveNames.getY())]])
        while repeat:
            UI_REFRESH_RATE = self.__window.getClock().tick(60)/1000
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    repeat = not repeat
                self.__manager.process_events(event)
            self.__manager.update(UI_REFRESH_RATE)
            self.__window.getScreen().fill((0,0,0))
            self.__window.getScreen().blit(self.__background, (0,0))
            self.__manager.draw_ui(self.__window.getScreen())
            for i in btnPos:
                self.__window.getScreen().blit(i[0],i[1])
            pg.display.flip()
            self.__window.getClock().tick(60)
        pg.quit()
from .frontend.GameObjects import GameObject
from .frontend.Window import Window
from .frontend.Btn import Btn
from . import ValueGame as VG
from .frontend.Draw import Draw
from .frontend.InputText import InputText
from .frontend.Collision import Collision
import pygame as pg
import pygame_gui as pg_ui


class GetDataInput(GameObject):
    def __init__(self, window: Window, title, x, y, width, height, isAvailable=True):
        super().__init__(x, y, width, height, isAvailable)
        self.__window = window

    def setImagesBackround(self, background):
        self.__background = pg.image.load(VG.VG_IMG_PATH+background)
        self.__background = pg.transform.scale(
            self.__background, (self._width, self._height))
        self.__approve = Btn("Approve.jpg", int(
            self._x - self._width/4), int(self._y+self._height/4), 100, 100)
        self.__decline = Btn("Decline.jpg", int(
            self._x + self._width/4), int(self._y+self._height/4), 100, 100)

    def getText(self,title="Wpisz tu swój text"):
        repeat = True
        toReturn = None
        listObject = Draw.transfomrToCenter(self.__createListObject())
        inputTextObject = InputText("#inputValue", title,self._x, int(self._y/4*3), 400, 50)
        MANAGER = pg_ui.UIManager(VG.SIZE)
        TEXT_INPUT = pg_ui.elements.UITextEntryLine(relative_rect=pg.Rect((int(inputTextObject.getX()-inputTextObject.getWidth()/2), inputTextObject.getY()),
                                                                          (int(inputTextObject.getWidth()), inputTextObject.getHeight())),
                                                    manager=MANAGER,
                                                    object_id=inputTextObject.getId())
        TEXT_INPUT.set_text(inputTextObject.getText())
        while repeat:
            UI_REFRESH_RATE = self.__window.getClock().tick(60)/1000
            for i in listObject:
                self.__window.getScreen().blit(i[0], i[1])
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN and Collision.isCollisionRectMouse(self.__approve):
                    repeat = False
                    toReturn = TEXT_INPUT.get_text()
                if event.type == pg.MOUSEBUTTONDOWN and Collision.isCollisionRectMouse(self.__decline):
                    repeat = False
                MANAGER.process_events(event)
            MANAGER.update(UI_REFRESH_RATE)
            MANAGER.draw_ui(self.__window.getScreen())
            pg.display.update()
            self.__window.getClock().tick(60)
        return toReturn
    def __createListObject(self):
        toReturn = []
        toReturn.append([self.__background, (self._x, self._y)])
        toReturn.append([self.__approve.getImage(),
                        (self.__approve.getX(), self.__approve.getY())])
        toReturn.append([self.__decline.getImage(),
                        (self.__decline.getX(), self.__decline.getY())])
        return toReturn

from . import ValuesFrontend as VF
from .InputText import InputText

import pygame_gui as pg_ui
import pygame as pg
class CreateManagerInputs:
    @staticmethod
    def createManagerInputs(inputsList,windowSize):
        MANAGER =pg_ui.UIManager((windowSize))
        for i in range(len(inputsList)):
            tmp= inputsList[i]
            inputVal = pg_ui.elements.UITextEntryLine(relative_rect=pg.Rect(((tmp.getX(),tmp.getY()),
                                                                          (tmp.getWidth(),tmp.getHeight())), 
                                                                         manager=MANAGER,
                                                                         object_id = tmp.getId()))
            inputVal.set_text(tmp.getText())
        return MANAGER
    
    
    @staticmethod
    def createInputsList(numOfInputs,screenSize,textInput,idName):
        inputs = []
        windowPart = int(screenSize[1] / numOfInputs)
        y = int(windowPart/2)
        for i in range(numOfInputs):
            playerName = idName+str(i+1)
            inputVal = InputText("#"+playerName,textInput+playerName,50,y,500,50)
            inputs.append(inputVal)
            y+=windowPart
        return inputs
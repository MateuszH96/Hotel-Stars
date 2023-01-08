from . import GameObjects as GO


class InputText(GO.GameObject):
    #klasa odpowiedzialna za przechowywanie danych z inputów
    def __init__(self, id, text, x, y, width, height, isAvailable=True):
        super().__init__(x, y, width, height, isAvailable)
        self.__id = id
        self.__text = text

    def getId(self):
        return self.__id

    def getText(self):
        return self.__text

    def setText(self, inputText):
        self.__text = inputText

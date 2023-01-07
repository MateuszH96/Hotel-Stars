
class Window:
    def __init__(self,clock,screen):
        self.__clock = clock
        self.__screen = screen
        
    def getScreen(self):
        return self.__screen
    
    def getClock(self):
        return self.__clock
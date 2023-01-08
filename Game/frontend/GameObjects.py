class GameObject:
    #klasa nadrzędna obiektów występujących w grze
    def __init__(self,x=0,y=0,width=0,height=0,isAvailable=True):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._isAvailable = isAvailable
    
    def getX(self):
        return self._x
    
    def getY(self):
        return self._y
    
    def getWidth(self):
        return self._width
    
    def getHeight(self):
        return self._height
    
    def getAvailable(self):
        return self._isAvailable
    
    def setAvailable(self,status):
        self._isAvailable = status
    
    def draw(self):
        pass
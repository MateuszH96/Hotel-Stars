from .Img import Img

class Draw:
    @staticmethod
    def transfomrToCenter(objectsToMove):
        toReturn = []
        for i in objectsToMove:
            x = i[1][0]
            y = i[1][1]
            centerX = i[0].get_rect().centerx
            centerY = i[0].get_rect().centery
            toReturn.append([i[0], (x-centerX, y-centerY)])
        return toReturn
    pass

    @staticmethod
    def draw(toDraw,window):
        for i in toDraw:
            window.blit(i[0],i[1])

    @staticmethod
    def getImgValuesToCenter(img):
        return [img.getImage(),(img.getX(),img.getY())]
    
    @staticmethod
    def drawRectancgleBorder(img: Img, screen):
        widthRec = img.getWidth()
        heightRec = img.getHeight()
        xRec = img.getX()
        yRec = img.getY
        
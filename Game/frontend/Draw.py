class Draw:
    @staticmethod
    def transfomrToCenter(objectsToMove):
        toReturn=[]
        for i in objectsToMove:
            x = i[1][0]
            y = i[1][1]
            centerX = i[0].get_rect().centerx
            centerY = i[0].get_rect().centery
            toReturn.append([i[0],(x-centerX,y-centerY)])
        return toReturn
    pass
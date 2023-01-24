from .backend.Player import Player
from .frontend.Btn import Btn
from math import nan
class BtnBuyRoom(Btn):
    def __init__(self, image, x=0, y=0, width=0, height=0, isAvailable=True):
        super().__init__(image, x, y, width, height, isAvailable)
        
    def __findFirstZero(self,listToFindValue):
        for i in listToFindValue:
            for j in i:
                if j.getRoomLevel() == 0:
                    return (listToFindValue.index(i),i.index(j))
        return nan
        
    def onClick(self, player: Player):
        if player.getMoney() >= 500:
            index = self.__findFirstZero(player.getHotel().getAllFloor())
            if not(index is nan):
                floor,room = index
                player.getHotel().changeLevelRoom(floor,room)
            player.subMoney(500)
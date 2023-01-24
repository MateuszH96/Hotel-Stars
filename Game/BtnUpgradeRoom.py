from .backend.Player import Player
from .frontend.Btn import Btn

class BtnUpgradeRoom(Btn):
    def __init__(self, image, x=0, y=0, width=0, height=0, isAvailable=True):
        super().__init__(image, x, y, width, height, isAvailable)
        
    def onClick(self, player: Player, floor,room):
        if player.getMoney() >= 2000 and player.getHotel().getRoomLevel(floor,room).getRoomLevel() > 0 and player.getHotel().getRoomLevel(floor,room).getRoomLevel() < 4:
            player.getHotel().changeLevelRoom(floor,room)
            player.subMoney(2000)
        pass
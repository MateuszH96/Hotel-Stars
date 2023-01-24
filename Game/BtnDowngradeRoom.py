from .backend.Player import Player
from .frontend.Btn import Btn

class BtnDowngradeRoom(Btn):
    def __init__(self, image, x=0, y=0, width=0, height=0, isAvailable=True):
        super().__init__(image, x, y, width, height, isAvailable)
        
    def onClick(self, player: Player, floor,room):
        player.getHotel().changeLevelRoom(floor,room,False)
        player.addMoney(200)
        pass
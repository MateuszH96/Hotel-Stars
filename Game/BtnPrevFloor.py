from .frontend.Btn import Btn
from .backend.Player import Player
class BtnPrevFloor(Btn):
    def __init__(self, image, x=0, y=0, width=0, height=0, isAvailable=True):
        super().__init__(image, x, y, width, height, isAvailable)
    
    def onClick(self,player: Player):
        floorHotel = player.getFloorNum()
        if not (floorHotel - 1 < 0):
            player.setFloor(floorHotel-1)
    
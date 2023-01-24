from .frontend.Btn import Btn
from .backend.Player import Player

class BtnPassRound(Btn):
    def __init__(self, image, x=0, y=0, width=0, height=0, isAvailable=True):
        super().__init__(image, x, y, width, height, isAvailable)
        
    def onClick(self, player: Player):
        player.setPassRound(True)
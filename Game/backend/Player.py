from . import ValuesBacked as VB
from .Hotel import Hotel
from .Location import Location
from .Bank import Bank


class Player:
    """
        Class is responsible for operations like create and update a player and its attributes
    """

    # Constructors
    def __init__(self, name, location):
        self.__name = name
        self.__money = VB.INITIAL_MONEY
        self.__floor = 0
        self.__numberOfDebt = VB.INITIAL_DEBT
        self.__location = Location(location)
        self.__hotel = Hotel()
        self.__bank = Bank()

    # Getter
    def getFloorNum(self):
        return self.__floor
    def getHotel(self):
        return self.__hotel

    def getLocation(self):
        return self.__location

    def getBank(self):
        return self.__bank

    def getName(self):
        """
            Getter to return player name

            Returns:
                str: player name
        """
        return self.__name

    def getMoney(self):
        """
            Getter to return number of money

            Returns:
                str: number of money
       """
        return self.__money

    def getNumberOfDebt(self):
        """
            Getter to return number of debt

            Returns:
                str: number of debt
        """
        return self.__numberOfDebt

    def addFloorValue(self):
        self.__hotel.addFloor()

    #Setter
    def setFloor(self,floor):
        self.__floor = floor
    
    def setRoomLevelCostValue(self, indexOfLevel, costValue):
        """
        Setter to set room cost value

        Args:
            indexOfLevel (int): index of list cost
            costValue (float): Cost of rooms
        """
        self.__hotel.setRoomLevelCost(indexOfLevel, costValue)

    def changeLevelRoomValue(self, floor, room, upgrade=True):
        """Method resposible for upgrade/downgrade room

        Args:
            floor (int): Floor where is room
            room (int): number of room
            upgrade (bool): Boolean arg which set to upgrade or downgrade selected room. Defaults to True.

        Returns:
            bool: Resposne inform that level of room has been successfully changed
        """

        return self.__hotel.changeLevelRoom(floor, room, upgrade)

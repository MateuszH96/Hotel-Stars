from . import ValuesBacked as VB
from . import Hotel
from . import Location
from . import Bank


class Player:
    """
        Class is responsible for operations like create and update a player and its attributes
    """

    # Constructors
    def __init__(self, playerName, typeOfLocation):
        self.__playerName = playerName
        self.__numberOfMoney = VB.INITIAL_MONEY
        self.__numberOfDebt = VB.INITIAL_DEBT
        self.__location = Location.Location(typeOfLocation)
        self.__hotel = Hotel.Hotel()
        self.__bank = Bank.Bank()

    # Getter

    def getHotel(self):
        return self.__hotel

    def getLocation(self):
        return self.__location

    def getBank(self):
        return self.__bank

    def getPlayerName(self):
        """
            Getter to return player name

            Returns:
                str: player name
        """
        return self.__playerName

    def getNumberOfMoney(self):
        """
            Getter to return number of money

            Returns:
                str: number of money
       """
        return self.__numberOfMoney

    def getNumberOfDebt(self):
        """
            Getter to return number of debt

            Returns:
                str: number of debt
        """
        return self.__numberOfDebt

    def addFloorValue(self):
        self.__hotel.addFloor()

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

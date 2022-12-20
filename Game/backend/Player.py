from ValuesBacked import *
from Location import Location
from Hotel import Hotel
from Bank import Bank
from math import nan,floor

class Player:
    """
        Class is responsible for operations like create and update a player and its attributes
    """

    # Constructors
    def __init__(self, playerName, typeOfLocation):
        self.__playerName = playerName
        self.numberOfMoney = INITIAL_MONEY
        self.numberOfDebt = INITIAL_DEBT
        self.__typeOfLocation = typeOfLocation
        self.location = Location(typeOfLocation)
        self.hotel = Hotel()
        self.bank = Bank()

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
        return self.numberOfMoney

    def getNumberOfDebt(self):
        """
            Getter to return number of debt

            Returns:
                str: number of debt
        """
        return self.numberOfDebt

    def addFloorValue(self):
        self.hotel.addFloor()

    def getFloorValue(self, index=0):
        """Getter to return listo of rooms in floor
        Args:
            index (int): Number of floor to return. Defaults to 0.

        Returns:
            List: List of rooms in selected floor
        """
        return self.hotel.getFloor(index)

    def getAllFloorValue(self):
        """Getter to return list of flors in hotel

        Returns:
            List: List of floors in Hotel
        """
        return self.hotel.getAllFloor()

    def getLevelRoomCostValue(self, level):
        """_summary_

        Args:
            level (_type_): _description_

        Returns:
            _type_: _description_
        """
        return self.hotel.getLevelRoomCost(level)

    def setRoomLevelCostValue(self, indexOfLevel, costValue):
        """
        Setter to set room cost value

        Args:
            indexOfLevel (int): index of list cost
            costValue (float): Cost of rooms
        """
        self.hotel.setRoomLevelCost(indexOfLevel, costValue)

    def changeLevelRoomValue(self, floor, room, upgrade=True):
        """Method resposible for upgrade/downgrade room

        Args:
            floor (int): Floor where is room
            room (int): number of room
            upgrade (bool): Boolean arg which set to upgrade or downgrade selected room. Defaults to True.

        Returns:
            bool: Resposne inform that level of room has been successfully changed
        """

        return self.hotel.changeLevelRoom(floor, room, upgrade)

    def getAllEployeesValue(self):
        """Getter to return number of employees

        Returns:
            int: _description_
        """
        return self.hotel.getAllEployees()

    def getAllRoomsNumValue(self):
        """Getter to return number of all rooms

        Returns:
            _type_: _description_
        """
        return  self.hotel.getAllRoomsNum()

    def getRoomLevelValue(self, floor, numberOfRoom):
        """_summary_

        Args:
            floor (int): _description_
            numberOfRoom (int): _description_

        Returns:
            _type_: _description_
        """
        return self.hotel.getRoomLevel(floor, numberOfRoom)


    def getNumberOfCustomersValue(self):
        """
            Getter to return number of customers

            Returns:
                int: Number of customers
        """
        return self.location.getNumberOfCustomers()


    def getNumberOfVipCustomersValue(self):
        """
            Getter to return number of vip clients

            Returns:
                int: Number of vip customers
        """
        return self.location.getNumberOfVipCustomers()

    def getNumberOfNormalCustomersValue(self):
        """
            Getter to return number of normal clients

            Returns:
                int: Number of vip customers
        """
        return self.location.getNumberOfNormalCustomers()

    def setNewNumberOfCustomers(self, newNumberOfCustomers):
        """
            Setter to set room cost value

            Returns:
             int: new number of Customers
        """
        self.location.setNewNumberOfCustomers(newNumberOfCustomers)

    def getCreditorthinessValue(self):
        """
            Getter to return creditworthiness

            Returns:
                int: creditworthiness
        """
        return self.bank.getCreditorthiness()


    def upgradeNumberOfMoney(self):
        """
            Function is responsible for upgrade money

        """
        pass

    def downgradeNumberOfMoney(self):
        """
            Function is responsible for downgrade money

        """
        pass

    def upgradeNumberOfDebt(self):
        """
            Function is responsible for upgrade debt

        """
        pass

    def downgradeNumberOfDebt(self):
        """
            Function is responsible for downgrade debt

        """
        pass

    def repayTheDebt(self):
        """
            Function is responsible for repay the debt
        """
        pass

    def takeADebt(self):
        """
            Function is responsible for take a debt
        """
        pass


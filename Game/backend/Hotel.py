from . import ValuesBacked as VB
from . import Room
from math import nan,floor

class Hotel:
    """
    
    """
    # Constructor

    def __init__(self):
        """Constructor
        """
        self.__floors = []
        self.__roomCost = VB.FLOOR_COST_INITIAL
        self.addFloor()

    # Private
    
    
    # Public
    def addFloor(self):
        """Method resposible for add floor in hotel
        """
        self.__floors.append([Room.Room() for x in range(VB.ROOMS_PER_FLOOR)])


    def getFloor(self, index=0):
        """Getter to return listo of rooms in floor
        Args:
            index (int): Number of floor to return. Defaults to 0.

        Returns:
            List: List of rooms in selected floor 
        """
        return self.__floors[index]


    def getAllFloor(self):
        """Getter to return list of flors in hotel

        Returns:
            List: List of floors in Hotel
        """
        return self.__floors
    
    
    def getLevelRoomCost(self, level):
        """_summary_

        Args:
            level (_type_): _description_

        Returns:
            _type_: _description_
        """
        if level < len(self.__roomCost) and level >= 0:
            return self.__roomCost[level]
        return nan

    def setRoomLevelCost(self, indexOfLevel, costValue):
        """
        Setter to set room cost value

        Args:
            indexOfLevel (int): index of list cost 
            costValue (float): Cost of rooms 
        """
        self.__roomCost[indexOfLevel] = costValue
        

    def changeLevelRoom(self,floor, room, upgrade=True):
        """Method resposible for upgrade/downgrade room

        Args:
            floor (int): Floor where is room
            room (int): number of room
            upgrade (bool): Boolean arg which set to upgrade or downgrade selected room. Defaults to True.

        Returns:
            bool: Resposne inform that level of room has been successfully changed
        """
        if upgrade:
            return self.__floors[floor][room].upgradeRoom()
        return self.__floors[floor][room].downgradeRoom()
    
    def getAllEployees(self):
        """Getter to return number of employees

        Returns:
            int: _description_
        """
        toReturn = 0
        for i in self.__floors:
            for j in i:
                toReturn += j.getEmployeeValue()
        
        toReturn = floor(toReturn)
        return toReturn
    
    def getAllRoomsNum(self):
        """Getter to return number of all rooms

        Returns:
            _type_: _description_
        """
        toReturn = 0
        for i in self.__floors:
            for j in i:
                if j.getRoomLevel() != 0:
                    toReturn+=1
        return toReturn
    
    def getRoomLevel(self, floor, numberOfRoom):
        """_summary_

        Args:
            floor (int): _description_
            numberOfRoom (int): _description_

        Returns:
            _type_: _description_
        """
        return self.__floors[floor][numberOfRoom]
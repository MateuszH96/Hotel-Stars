from . import ValuesBacked as VB
from .Room import Room
from math import nan, ceil


class Hotel:
    # Constructor

    def __init__(self):
        self.__floors =[]
        self.__roomCost = VB.FLOOR_COST_INITIAL
        self.__salary = 1000
        self.addFloor()

    def addFloor(self):
        self.__floors.append([Room() for x in range(VB.ROOMS_PER_FLOOR)])

    def getSalary(self):
        return self.__salary
    
    def setSalaty(self,val):
        self.__salary = val
    
    def getFloor(self, index=0):
        return self.__floors[index]

    def getAllFloor(self):
        return self.__floors

    def getRoomCost(self):
        return self.__roomCost
    
    def getLevelRoomCost(self, level):
        if level < len(self.__roomCost) and level >= 0:
            return self.__roomCost[level]
        return nan

    def setRoomLevelCost(self, indexOfLevel, costValue):
        self.__roomCost[indexOfLevel] = costValue

    def changeLevelRoom(self, floor, room, upgrade=True):
        if upgrade:
            return self.__floors[floor][room].upgradeRoomLvl()
        return self.__floors[floor][room].downgradeRoomLvl()

    def getAllEployees(self):
        toReturn = 0
        for i in self.__floors:
            for j in i:
                toReturn += j.getEmployeeValue()

        toReturn = ceil(toReturn)
        return toReturn

    def getAllRoomsNum(self):
        toReturn = 0
        for i in self.__floors:
            for j in i:
                if j.getRoomLevel() != 0:
                    toReturn += 1
        return toReturn

    def getRoomLevel(self, floor, numberOfRoom):
        return self.__floors[floor][numberOfRoom]

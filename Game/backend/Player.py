from . import ValuesBacked as VB
from .Hotel import Hotel
from .Location import Location
from .Bank import Bank

import math

class Player:
    # Constructors
    def __init__(self, name, location):
        self.__name = name[:10]
        self.__money = VB.INITIAL_MONEY
        self.__floor = 0
        self.__numberOfDebt = VB.INITIAL_DEBT
        self.__isLoan = False
        self.__round = -1
        self.__location = Location(location)
        self.__hotel = Hotel()
        self.__bank = Bank()
        self.__passRound = False
        self.__passTurn = False
        self.__customerHappinesPtr = 1
        self.__employeesHappinesPtr = 1
        self.__debtRatio = 1
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
        return self.__name

    def getMoney(self):
        return self.__money

    def getNumberOfDebt(self):
        return self.__numberOfDebt

    def getLoanStatus(self):
        return self.__isLoan
    
    def getRound(self):
        return self.__round

    def getPassTurn(self):
        return self.__passTurn
    
    def getPassRound(self):
        return self.__passRound
    
    def addFloor(self):
        self.__hotel.addFloor()

    #Setter
    def setRound(self,val):
        self.__round = val
    def setPassTurn(self, val):
        self.__passTurn = val

    def addMoney(self,val):
        self.__money += val
    
    def subMoney(self,val):
        self.__money -= val
    def setPassRound(self, val):
        self.__passRound = val
    
    def setLoanStatus(self, status):
        self.__isLoan = True
    
    def setFloor(self,floor):
        self.__floor = floor
    
    def setRoomLevelCostValue(self, indexOfLevel, costValue):
        self.__hotel.setRoomLevelCost(indexOfLevel, costValue)

    def changeLevelRoomValue(self, floor, room, upgrade=True):
        return self.__hotel.changeLevelRoom(floor, room, upgrade)

    def nextRound(self):
        self.__round += 1
        
    def CalcEndRound(self):
        self.__earnMoney()
    
    def __earnMoney(self):
        earnMoneyValue = 0
        roomList = self.__hotel.getAllFloor()
        VIPcustomer = self.__location.getNumberOfVipCustomers()
        classicCustomer = self.__location.getNumberOfNormalCustomers()
        
        tmpVIPCustomer = VIPcustomer
        tmpClassicCustomer = classicCustomer
        
        for floor in roomList:
            for room in floor:
                roomLvl = room.getRoomLevel()
                if roomLvl == 1 or roomLvl == 2:
                    if tmpClassicCustomer >= 3:
                        earnMoneyValue += self.__hotel.getRoomCost()[roomLvl]*3
                        tmpClassicCustomer-=3
                    else:
                        earnMoneyValue += self.__hotel.getRoomCost()[roomLvl]*tmpClassicCustomer
                        tmpClassicCustomer=0
                elif roomLvl == 3 or roomLvl == 4:
                    if tmpVIPCustomer >= 3:
                        earnMoneyValue += self.__hotel.getRoomCost()[roomLvl]*3
                        tmpVIPCustomer-=3
                    else:
                        earnMoneyValue += self.__hotel.getRoomCost()[roomLvl]*tmpVIPCustomer
                        tmpVIPCustomer=0
                        tmpVIPCustomer-=3
        earnMoneyValue *= 0.9
        earnMoneyValue -= self.__hotel.getSalary() * self.__hotel.getAllEployees()
        earnMoneyValue  = math.floor(earnMoneyValue)
        self.__money += earnMoneyValue
        self.__bank.addEarnings(earnMoneyValue)
        if self.__isLoan:
            self.__money -= self.__bank.getLoanInstallmentValue()
            self.__bank.payTheInstallment()
        if self.__round >= 0 and self.__round <= 3:
            self.__money += VB.INITIAL_MONEY
        #zadowolenie klientów
        customerHappines =1 - (tmpVIPCustomer/VIPcustomer) - (tmpClassicCustomer/classicCustomer)
        self.__parametersToWin(customerHappines)
        self.__hotel.setSalaty(self.__hotel.getSalary()+ 150)
        self.__location.changeTurn()
        pass
    
    def __parametersToWin(self,customerHappines):
        self.__customerHappinesPtr *= customerHappines
        if self.__money < 0:
            self.__employeesHappinesPtr * 0.8
        debt = 0
        if self.__isLoan:
            debt = self.__bank.getLoanToReturn()
        self.__debtRatio = 1+self.__money/(debt + math.abs(self.__money))
        pass
    def getResult(self):
        return self.__debtRatio  * self.__customerHappinesPtr * self.__employeesHappinesPtr
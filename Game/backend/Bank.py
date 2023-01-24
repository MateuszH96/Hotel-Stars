from . import ValuesBacked as VB
from statistics import mean
from math import ceil


class Bank:

    def __init__(self):
        self.__earnings = VB.EARN_LIST
        self.__loanToReturn = 0
        self.__loanInstallment = 0
    def addEarnings(self, earnings):
        if len(self.__earnings) < VB.LAST_FOUR_QUARTERS:
            self.__earnings.append(earnings)
        else:
            self.__earnings.pop(0)
            self.__earnings.append(earnings)

    def getCreditorthiness(self):  # funkcja podaje wartość na jaką można wziąć kredyt
        return mean(self.__earnings) / VB.DIVIDER

    def payTheInstallment(self, money= 0):
        if money == 0:
            money = self.__loanInstallment
        if self.__loanToReturn - money > self.__loanInstallment:
            self.__loanToReturn -= money
        elif self.__loanToReturn - money < self.__loanInstallment and self.__loanToReturn - money> 0:
            self.__loanInstallment = self.__loanToReturn - money
            self.__loanToReturn -= money
        else:
            self.__loanToReturn = 0
            self.__loanInstallment = 0
            
    def getCredit(self, money):
        if self.getCreditorthiness() <= money:
            self.__loanToReturn = money + 0.2 * money
            self.__loanInstallment = ceil(self.__loanToReturn /10)
            return money
        return 0
    def getLoanInstallmentValue(self):
        return self.__loanInstallment
    
    def getLoanToReturn(self):
        return self.__loanToReturn
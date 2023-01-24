from random import uniform
from math import floor
from . import ValuesBacked as VB


class Location:
    # Constructors
    def __init__(self, typeOfLocation):
        self.__numberOfCustomers = VB.INITIAL_NUMBER_OF_CUSTOMERS
        self.__ptrVIP = VB.LOCATION_VIP_PTR[typeOfLocation]
        self.__generateNewNumberOfCustomer()

    def getNumberOfVipCustomers(self):
        return self.__numOfVIP

    def getNumberOfNormalCustomers(self):
        return self.__numberOfCustomers - self.__numOfVIP

    def changeTurn(self):  # wywoałnie zmiany tury
        self.__generateNewNumberOfCustomer()

    def __generateNewNumberOfCustomer(self, dwBand=VB.DW_BAND, upBand=VB.UP_BAND):
        # generowanie nowej liczby gości i vipów, normalni są obliczani jako wszyscy-VIP
        # upBand i dwBand są granicami przedziału losowania w przypadku bonusu można je zmieniać
        mulCustomers = uniform(dwBand, upBand)
        self.__numberOfCustomers = floor(
            self.__numberOfCustomers * mulCustomers)
        self.__numOfVIP = floor(
            self.__numberOfCustomers * uniform(0, self.__ptrVIP))

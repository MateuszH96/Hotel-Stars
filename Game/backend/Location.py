from ValuesBacked import *
from random import uniform
from math import floor
class Location:
    """
        Class is responsible for operations like create a Location
    """

    # Constructors
    def __init__(self, typeOfLocation):
        self.__numberOfCustomers = INITIAL_NUMBER_OF_CUSTOMERS
        self.__ptrVIP = LOCATION_VIP_PTR[typeOfLocation]

    def getNumberOfVipCustomers(self):
        """
            Getter to return number of vip clients

            Returns:
                int: Number of vip customers
        """
        return self.__numOfVIP

    def getNumberOfNormalCustomers(self):
        """
            Getter to return number of normal clients

            Returns:
                int: Number of vip customers
        """
        return self.__numberOfCustomers - self.__numOfVIP
    
    def changeTurn(self): #wywoałnie zmiany tury
        self.__generateNewNumberOfCustomer()
    
    def __generateNewNumberOfCustomer(self,dwBand=DW_BAND,upBand=UP_BAND): 
        #generowanie nowej liczby gości i vipów, normalni są obliczani jako wszyscy-VIP 
        #upBand i dwBand są granicami przedziału losowania w przypadku bonusu można je zmieniać
        mulCustomers = uniform(dwBand,upBand)
        self.__numberOfCustomers = floor(self.__numberOfCustomers * mulCustomers)
        self.__numOfVIP = floor(self.__numberOfCustomers * uniform(0,self.__ptrVIP))
    
    
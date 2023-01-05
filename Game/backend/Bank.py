from ValuesBacked import *
from statistics import mean

class Bank:
    """
        The class is responsible for all banking operations

    """

    # Constructors 
    def __init__(self):
        """Constructor
        """
        self.__earnings = EARN_LIST 
        self.sumEarnings()
    
    #Public 
    def addEarnings(self, earnings):
        """Method resposible for adding new earnings to the list
        """
        if len(EARN_LIST) < LAST_FOUR_QUARTERS:
            self.__earnings.append(earnings)
        else:
            self.__earnings.pop(0)
            self.__earnings.append(earnings)

    def getCreditorthiness(self):#funkcja podaje wartość na jaką można wziąć kredyt
        return mean(self.__earnings)/ DIVIDER
    
    def getCredit(self,money):
        if self.getCreditorthiness <= money:
            return money
        return 0
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
    def sumEarnings(self):
        """Method resposible for adding up the earnings
        """
        self.__earnings.sum([Bank() for x in range(len(EARN_LIST))])

    def addEarnings(self):
        """Method resposible for adding new earnings to the list
        """
        if len(EARN_LIST) < 4:
            self.__earnings.append([Bank() for x in range(EARN_LIST)])
        if len(EARN_LIST) == 4:
            self.__earnings.pop(0)
            self.__earnings.append([Bank() for x in range(EARN_LIST)])

    def getCreditorthiness(self):
        self.__creditworthiness = mean(self.__earnings)/ DIVIDER
        """
        Getter to return creditworthiness

        Returns:
            int: creditworthiness
        """
        return self.__creditworthiness
    
    def getCredit(self):
         """
        Getter to return credit

        Returns:
            int: credit
        """




    
 


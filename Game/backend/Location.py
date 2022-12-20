from ValuesBacked import *


class Location:
    """
        Class is responsible for operations like create a Location
    """

    # Constructors
    def __init__(self, typeOfLocation):
        self.locationValuesList = INITIAL_LOCATION_VALUES_LIST
        self.numberOfCustomers = INITIAL_NUMBER_OF_CUSTOMERS
        self.numberOfNormalCustomers = int(self.numberOfCustomers * self.locationValuesList[INITIAL_LOCATION_NAME_LIST.index(typeOfLocation)])
        self.numberOfVipCustomers = self.numberOfCustomers - self.numberOfNormalCustomers


    def getNumberOfCustomers(self):
        """
            Getter to return number of customers

            Returns:
                int: Number of customers
        """
        return self.numberOfCustomers

    def getNumberOfVipCustomers(self):
        """
            Getter to return number of vip clients

            Returns:
                int: Number of vip customers
        """
        return self.numberOfVipCustomers

    def getNumberOfNormalCustomers(self):
        """
            Getter to return number of normal clients

            Returns:
                int: Number of vip customers
        """
        return self.numberOfNormalCustomers


    def setNewNumberOfCustomers(self, newNumberOfCustomers):
        """
            Setter to set room cost value

            Returns:
             int: new number of Customers
        """
        self.numberOfNormalCustomers = newNumberOfCustomers

    def setNewLocationValuesList(self):
        pass
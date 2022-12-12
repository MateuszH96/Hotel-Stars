from ValuesBacked import *

class Room:
    """
        Class is resposible for operations like create, update o increase level of Room
    """
    # Constructors
    def __init__(self):
        self.__listEmployees=EMPLOYEE_LIST_NUM
        self.__setValues(VIP_FALSE,ROOM_LEVEL_INITIAL_VALUE)
            
    # Private
    def __setValues(self,isVip, roomLvl):
        self.__isVip = isVip
        self.__roomLevel = roomLvl
        self.__employeesPointer = self.__listEmployees[self.__roomLevel]
        
    # Public
    def upgradeRoomLvl(self):
        """
        Function is resposible for for upgrade Room

        Returns:
            bool: Returns True when room level successfully demolished, otherwise false
        """
        if self.__roomLevel + 1 == len(self.__listEmployees):
            self.__setValues(VIP_TRUE, self.__roomLevel + 1)
        elif self.__roomLevel + 1 < len(self.__listEmployees):
            self.__setValues(VIP_FALSE, self.__roomLevel + 1)
        else:
            return False
        return True
    
    
    
    def downgradeRoomLvl(self):
        """
        Function is resposible for for downgrade Room

        Returns:
            bool: Returns True when room level successfully raised, otherwise false
        """
        if self.__roomLevel - 1 != 0:
            self.__setValues(VIP_FALSE, self.__roomLevel - 1)
        else:
            return False
        return True
        
    
    def getRoomLevel(self):
        """
        Getter to return level of room

        Returns:
            int: Room Level
        """
        return self.__roomLevel
    
    
    def getVipStatus(self):
        """
        Getter to return VIP status room 
        Returns:
            bool: VIP status room
        """
        return self.__isVip
    
    
    def getEmployeeValue(self):
        """
        Getter to return value of employees 

        Returns:
            float: pointer of employee
        """
        return self.__employeesPointer

a = Room()
b = Room()
lista = [[a, 0],[]]
lista[0][1] = b
print(lista)
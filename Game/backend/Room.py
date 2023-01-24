from . import ValuesBacked as VB


class Room:

    def __init__(self):
        self.__listEmployees = VB.EMPLOYEE_LIST_NUM
        self.__setValues(VB.VIP_FALSE, VB.ROOM_LEVEL_INITIAL_VALUE)

    def __setValues(self, isVip, roomLvl):
        self.__isVip = isVip
        self.__roomLevel = roomLvl
        self.__employeesPointer = self.__listEmployees[self.__roomLevel]

    def upgradeRoomLvl(self):
        if self.__roomLevel + 1 == len(self.__listEmployees):
            self.__setValues(VB.VIP_TRUE, self.__roomLevel + 1)
        elif self.__roomLevel + 1 < len(self.__listEmployees):
            self.__setValues(VB.VIP_FALSE, self.__roomLevel + 1)
        else:
            return False
        return True

    def downgradeRoomLvl(self):
        if self.__roomLevel - 1 != 0:
            self.__setValues(VB.VIP_FALSE, self.__roomLevel - 1)
        else:
            return False
        return True

    def getRoomLevel(self):

        return self.__roomLevel

    def getVipStatus(self):
        return self.__isVip

    def getEmployeeValue(self):
        return self.__employeesPointer

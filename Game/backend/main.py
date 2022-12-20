from Location import Location
from Player import Player


def main():
    p = Player('xxx','CENTER')
    print(p.location.getNumberOfCustomers())
    print(p.location.getNumberOfNormalCustomers())
    print(p.location.getNumberOfVipCustomers())


main()

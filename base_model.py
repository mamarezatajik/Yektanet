class BaseAdvertising:
    __allClicks = 0

    def __init__(self):
        self.__clicks = 0
        self.__views = 0

    def getClicks(self):
        print(self.__clicks)

    def getViewes(self):
        print(self.__views)

    def incClicks(self):
        BaseAdvertising.__allClicks += 1
        self.__clicks += 1

    def incViews(self):
        self.__views += 1

    def describeMe(self):
        print(f"your clicks are {self.__clicks} times")
        print(f"your views are {self.__views} times\n")
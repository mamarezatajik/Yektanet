from base_model import BaseAdvertising

class Advertiser(BaseAdvertising):
    def __init__(self, id, name):
        super().__init__()
        self.__id = id
        self.__name = name

    def getName(self):
        print(self.__name)

    def setName(self, name):
        self.__name = name

    @staticmethod
    def getTotalClicks():
        print(BaseAdvertising._BaseAdvertising__allClicks)


    def help():
        print("in this class we have 4 fields:")
        print("id, name, clicks and views")
        print("in addition we have 2 more fields:")
        print("allClicks and idNumber, that")
        print("shows number of users and all clicks of all users.\n")


    def describeMe(self):
        print(f"Your id is {self.__id}")
        print(f"Your name is {self.__name}")
        super().describeMe()
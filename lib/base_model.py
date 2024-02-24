class BaseAdvertising:
    __allClicks = 0

    def __init__(self):
        self.__clicks = 0
        self.__views = 0

    def get_clicks(self):
        return self.__clicks

    def get_viewes(self):
        return self.__views

    def inc_clicks(self):
        BaseAdvertising.__allClicks += 1
        self.__clicks += 1

    def inc_views(self):
        self.__views += 1


    @staticmethod        
    def describe_me():
        return "This is Base class"
from base_model import BaseAdvertising

class Advertiser(BaseAdvertising):
    id_numbers = set()


    def __init__(self, id, name):
        if id in Advertiser.id_numbers:
            print("This id has already been used")
            return 
        Advertiser.id_numbers.add(id)
        self.__id = id
        self.__name = name
        super().__init__()

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    @staticmethod
    def get_total_clicks():
        return BaseAdvertising._BaseAdvertising__allClicks

    @staticmethod
    def help():
        return "Advertiser field ---> id, name, clicks, views and all_veiws"

    @staticmethod
    def describe_me():
        return "This is Advertiser class"
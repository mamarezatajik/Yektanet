from base_model import BaseAdvertising

class Ad(BaseAdvertising):
    id_numbers = set()


    def __init__(self, id, title, imgUrl, link, advertiser):
        if id in Ad.id_numbers:
            print("This id has already been used")
            return 
        Ad.id_numbers.add(id)
        self.__id = id
        self.__title = title
        self.__imgUrl = imgUrl
        self.__link = link
        self.__advertiser = advertiser
        super().__init__()


    def get_title(self):
        print(self.__title)

    def set_title(self, title):
        self.__title = title

    def get_imgUrl(self):
        print(self.__imgUrl)

    def set_imgUrl(self, imgUrl):
        self.__imgUrl = imgUrl

    def get_link(self):
        print(self.__link)

    def set_link(self, link):
        self.__link = link

    def inc_clicks(self):
        self.__advertiser.inc_clicks()
        super().inc_clicks()

    def inc_views(self):
        self.__advertiser.inc_views()
        super().inc_views()

    def set_advertiser(self, advertiser):
        self.__advertiser = advertiser 

    @staticmethod
    def describe_me():
        return "This is Ad class"
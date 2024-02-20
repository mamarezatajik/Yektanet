from base_model import BaseAdvertising

class Ad(BaseAdvertising):
    def __init__(self, id, title, imgUrl, link, advertiser):
        super().__init__()
        self.__id = id
        self.__title = title
        self.__imgUrl = imgUrl
        self.__link = link
        self.__advertiser = advertiser


    def getTitle(self):
        print(self.__title)

    def setTitle(self, title):
        self.__title = title

    def getImgUrl(self):
        print(self.__imgUrl)

    def setImgUrl(self, imgUrl):
        self.__imgUrl = imgUrl

    def getLink(self):
        print(self.__link)

    def setLink(self, link):
        self.__link = link

    def incClicks(self):
        self.__advertiser.incClicks()
        super().incClicks()

    def incViews(self):
        self.__advertiser.incViews()
        super().incViews()

    def setAdvertiser(self, advertiser):
        self.__advertiser = advertiser 

    def describeMe(self):
        print(f"your title is {self.__title}")
        print(f"your imgUrl is {self.__imgUrl}")
        print(f"your link is {self.__link}")
        super().describeMe()
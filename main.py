from ad import *
from advertiser import *
from base_model import *

def main():
    baseAdvertising = BaseAdvertising()
    advertiser1 = Advertiser(1, "name1")
    advertiser2 = Advertiser(2, "name2")
    ad1 = Ad(1, "title1", "img-url1", "link1", advertiser1)
    ad2 = Ad(2, "title2", "img-url2", "link2", advertiser2)
    baseAdvertising.describeMe()
    ad2.describeMe()
    advertiser1.describeMe()
    ad1.incViews()
    ad1.incViews()
    ad1.incViews()
    ad1.incViews()
    ad2.incViews()
    ad1.incClicks()
    ad2.incClicks()
    advertiser2.getName()
    advertiser2.setName("new name")
    advertiser2.getName()
    ad1.getClicks()
    advertiser2.getClicks()
    Advertiser.getTotalClicks()
    Advertiser.help()

if __name__ == '__main__':
    main()
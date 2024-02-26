from django.db import models

# Create your models here.


class BaseAdvertising(models.Model):
    clicks = models.IntegerField(default = 0)
    views = models.IntegerField(default = 0)


    def inc_clicks(self):
        self.__clicks += 1
        self.save()

    def inc_views(self):
        self.__views += 1
        self.save()

    class Meta:
        abstract = True

    @classmethod
    def get_total_clicks(cls):
        return cls.objects.aggregate(models.Sum('clicks'))['clicks__sum']




class Advertiser(BaseAdvertising):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name



class Ad(BaseAdvertising):
    title = models.CharField(max_length = 200)
    imgUrl = models.CharField(max_length = 200)
    link = models.CharField(max_length = 200)
    advertiser = models.ForeignKey(Advertiser, on_delete = models.CASCADE)

    def inc_clicks(self):
        self.advertiser.inc_clicks()
        super().inc_clicks()

    def inc_views(self):
        self.advertiser.inc_views()
        super().inc_views()

    def __str__(self):
        return self.title
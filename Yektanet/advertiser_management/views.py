from django.shortcuts import render
from .models import *
# Create your views here.



def all_ads(request):
    advertisers = Advertiser.objects.all()

    for advertiser in advertisers:
        ads = advertiser.ads.all()
        for ad in ads:
            ad.inc_views()

    context = {'advertisers': advertisers}
    return render(request, 'advertiser_management/ads.html', context)


def ad_detail(request, ad_id):
    ad = Ad.objects.get(pk = ad_id)

    ad.inc_clicks()

    context = {'ad': ad}
    return render(request, 'advertiser_management/ad_detail.html', context)
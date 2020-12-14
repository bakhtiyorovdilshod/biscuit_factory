from django.http import Http404

from apps.biscuit.models import PriceList


def get_price(biscuit):
    try:
        return PriceList.objects.filter(biscuit=biscuit)
    except PriceList.DoesNotExist:
        return ({'error': 404})

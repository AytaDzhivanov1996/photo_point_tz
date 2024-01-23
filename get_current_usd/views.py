import requests
import json
import time

from django.conf import settings
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from django.core.serializers import serialize

from get_current_usd.models import Currency


class CurrencyAPIView(ListAPIView):

    def get(self, *args, **kwargs):
        queryset = Currency.objects.all().order_by('id')[10::-1]
        serialized_data = serialize("json", queryset)
        json_data = json.loads(serialized_data)
        response = requests.get(f"https://v6.exchangerate-api.com/v6/{settings.API_KEY}/latest/USD")

        currency_request = Currency.objects.create(
            usd=response.json()['conversion_rates']['USD'],
            rub=response.json()['conversion_rates']['RUB']
        )
        currency_request.save()
        time.sleep(10)
        return Response({"current_exchange_rate": {"usd": currency_request.usd, "rub": currency_request.rub, "date": currency_request.created_at},
                         "last_ten_requests": [obj['fields'] for obj in json_data]})


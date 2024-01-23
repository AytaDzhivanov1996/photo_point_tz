from django.urls import path

from get_current_usd.views import CurrencyAPIView

urlpatterns = [
    path('get_current_usd/', CurrencyAPIView.as_view())
]
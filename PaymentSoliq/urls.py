from django.urls import path
from .views import PaymentVIEW, Cashback_API

urlpatterns = [
    path("pay_money/", PaymentVIEW.as_view()),
    path("cashback/", Cashback_API.as_view()),
    # path(),
]

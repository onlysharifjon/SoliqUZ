from django.urls import path
from .views import PaymentVIEW

urlpatterns = [
    path("pay_money/", PaymentVIEW.as_view()),
    # path(),
]

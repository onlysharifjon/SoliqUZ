from django.urls import path
from .views import PaymentVIEW, Cashback_API_GET

urlpatterns = [
    path("pay_money/", PaymentVIEW.as_view()),
    path("cashback/<int:fiksal_seriya>/", Cashback_API_GET.as_view(),),
    # path(),
]

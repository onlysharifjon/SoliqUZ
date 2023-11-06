from django.urls import path, include

from .views import LoginUserSoliq, Register
urlpatterns = [
    path('login/', LoginUserSoliq.as_view()),
    path('register/', Register.as_view()),

]
from django.urls import path, include

from .views import LoginUserSoliq
urlpatterns = [
    path('login/', LoginUserSoliq.as_view()),

]

from django.urls import path
from App01.views import hello

urlpatterns = [
    path('', hello),
]

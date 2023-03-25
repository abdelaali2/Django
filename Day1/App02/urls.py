from django.urls import path
from App02.views import display_Author, display_Library, display_Potter

urlpatterns = [
    path("", display_Library),
    path("<author_Name>", display_Author),
    path("J. K. Rowling/Harry Potter", display_Potter),
]

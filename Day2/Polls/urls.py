from django.urls import path
from Polls.views import (
    view_all_Questions,
    view_question_details,
    MyLoginView,
    MyLogoutView,
)

urlpatterns = [
    path("", view_all_Questions),
    path("question/<int:q_id>", view_question_details),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
]

from django.urls import path
from . import views

app_name = "csspractice"
urlpatterns = [
    path("", views.top, name="top"),
    path("commentlist", views.commentView, name="commentview"),
    path("commentsubmit", views.commentSubmit, name="commentsubmit"),
    path("login", views.login, name="login"),
]
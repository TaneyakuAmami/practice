from django.urls import path
from . import views

app_name = "commentapps"
urlpatterns = [
    path("", views.commentView, name="commentview"),
    path("commentsubmit", views.commentSubmit, name="commentsubmit"),
]
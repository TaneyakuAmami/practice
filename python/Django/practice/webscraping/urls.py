from django.urls import path
from . import views

app_name = "webscraping"
urlpatterns = [
    path("", views.start, name="start"),
    path("execute", views.execute, name="execute"),
]
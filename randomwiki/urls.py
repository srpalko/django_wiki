from django.urls import path

from . import views

app_name = 'randomwiki'

urlpatterns = [
    path("", views.randomwiki, name="randomwiki")
]

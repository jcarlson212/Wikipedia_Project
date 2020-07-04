from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.entryPage, name="entry"),
    path("results/<str:query>", views.results, name="results"),
    path("create/newEntry", views.create, name="create")
]

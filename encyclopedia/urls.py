from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.entryPage, name="entry"),
    path("results/<str:query>", views.results, name="results"),
    path("create/newEntry", views.create, name="create"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("random/random", views.randomPage, name="random")
]

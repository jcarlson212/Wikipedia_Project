from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entryPage, name="entry"),
    path("wiki/results/<str:query>", views.results, name="results"),
    path("wiki/create/newEntry", views.create, name="create"),
    path("wiki/edit/<str:title>", views.edit, name="edit"),
    path("wiki/random/random", views.randomPage, name="random")
]

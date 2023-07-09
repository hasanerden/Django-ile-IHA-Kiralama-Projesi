from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("index", views.index, name="index"),
    path("categories", views.categories, name="categories"),
    path("iha/create", views.post_iha_create, name="post_iha_create"),
    path("iha/create", views.post_iha_create, name="post_iha_create"),
    path("iha/iha-lists", views.iha_datatable_index, name="iha_datatable"),
    path("iha/iha_update/<slug:slug>", views.iha_update, name="iha_update"),
    path("iha/iha_delete/<slug:slug>", views.post_iha_delete, name="iha_delete"),
    path("categoriy/<slug:slug>", views.iha_categoriy, name="iha_categoriy"),
    path("iha/<slug:slug>", views.iha_details, name="iha_details"),
]
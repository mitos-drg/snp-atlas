from django.urls import path

from . import views

app_name = "snp"
urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("<int:snp_id>/", views.annotations, name="annotations"),
]

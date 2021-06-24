from django.urls import path, re_path
from django.urls.resolvers import URLPattern
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('search', views.searchResoult, name="search"),
    path('product', views.product, name="product"),
]


from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('search/<int:id_category>', views.search_category, name="search_category"),
    path('producto/<int:idProd>', views.product, name="product"),
]


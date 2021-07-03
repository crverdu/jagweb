from django.conf.urls import include
from django.urls import path
from . import views


urlpatterns = [
    #Web Comercial
    path('', views.index, name="index"),
    path('producto/<int:idProd>', views.product, name="product"),
    path('about', views.about, name="about"),
    path('search/<int:id_category>', views.search_category, name="search_category"),

    #Usuarios
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register',views.RegistroUsuario.as_view(),name='register'),

    #Moderador
    path('moderador',views.ListarProducto.as_view(), name='prod_list'),
    path('producto/agregar/', views.AgregarProducto.as_view(),name="add_product"),
    path('producto/editar/<int:pk>',views.ActualizarProducto.as_view(),name="edit_produc"),
    path('producto/eliminar/<int:pk>',views.EliminarProducto.as_view(),name='del_product'),
    
]


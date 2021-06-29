from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('search/<int:id_category>', views.search_category, name="search_category"),
    path('producto/<int:idProd>', views.product, name="product"),
    path('producto/agregar/', views.FormularioProductoView.add_product,name="add_product"),
    path('producto/guardar',views.FormularioProductoView.proc_formulario,name='guardar_product'),
    path('producto/editar/<int:idProd>',views.FormularioProductoView.edit_produc,name="edit_produc"),
    path('producto/update/<int:idProd>',views.FormularioProductoView.upd_produc,name="upd_produc"),
    path('usuario/registrar',views.FormularioUsuarioView.add_user,name='user_reg'),
    path('usuario/guardar',views.FormularioUsuarioView.save_register,name='user_sav'),
    path('usuario/login',LoginView.as_view(template_name='login.html'), name='login'),
    path('usuario/logout',LogoutView.as_view(template_name='logout.html'), name='logout'),
]


from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),

    path('categorias/', views.listar_categorias, name='listar_categorias'),
    path('categorias/crear/', views.crear_categoria, name='crear_categoria'),
    path('categorias/editar/<int:id>/', views.editar_categoria, name='editar_categoria'),
    path('categorias/eliminar/<int:id>/', views.eliminar_categoria, name='eliminar_categoria'),

    path('prendas/', views.listar_prendas, name='listar_prendas'),
    path('prendas/crear/', views.crear_prenda, name='crear_prenda'),
    path('prendas/editar/<int:id>/', views.editar_prenda, name='editar_prenda'),
    path('prendas/eliminar/<int:id>/', views.eliminar_prenda, name='eliminar_prenda'),
]
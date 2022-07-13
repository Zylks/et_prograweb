from django import views
from django.urls import path, include
from .views import home, accesorios, contacto, comida, listar_contactos, registro, ContactoViewset,contacto_collection,contacto_element,agregar_alimento,listar_alimentos,modificar_alimento,eliminar_alimento,producto_collection,producto_element
from rest_framework import routers


router = routers.DefaultRouter()
router.register('contacto', ContactoViewset)
#localhost:8000/api/contacto/

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('accesorios/', accesorios, name="accesorios"),
    path('comida/', comida, name="comida"),
    path('agregar-alimento/', agregar_alimento, name="agregar_alimento"),
    path('listar-alimentos/', listar_alimentos, name="listar_alimentos"),
    path('modificar-alimento/<id>/', modificar_alimento, name="modificar_alimento"),
    path('eliminar-producto/<id>/', eliminar_alimento, name="eliminar_alimento" ),
    path('listar/', listar_contactos, name="listar"),
    path('registro/', registro, name="registro"),
    path('api/', include(router.urls)),
    path('contactos/', contacto_collection , name='contacto_collection'),
    path('contactos/<int:pk>/', contacto_element ,name='contacto_element'),
    path('alimento/', producto_collection , name='producto_collection'),
    path('alimento/<int:pk>/', producto_element ,name='producto_element'),
]
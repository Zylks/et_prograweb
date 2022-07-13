from .models import Contacto,Producto
from rest_framework import serializers

class ContactoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Contacto
        fields = "__all__"
        
class ProductoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Producto
        fields = "__all__"
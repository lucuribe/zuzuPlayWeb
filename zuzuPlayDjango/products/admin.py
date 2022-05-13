from django.contrib import admin
from .models import Usuario, Suscriptor, Categoria, Subcategoria, Marca, Producto, Unidad

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Suscriptor)
admin.site.register(Categoria)
admin.site.register(Subcategoria)
admin.site.register(Marca)
admin.site.register(Producto)
admin.site.register(Unidad)
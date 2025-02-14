from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Puesto)
admin.site.register(Miembro)
admin.site.register(Servicio)
admin.site.register(Partner)
admin.site.register(Comentario)
admin.site.register(ImagenesDeComentario)
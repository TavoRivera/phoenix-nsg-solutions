from modeltranslation.translator import register, TranslationOptions
from .models import Puesto, Miembro, Servicio, Partner

@register(Puesto)
class PuestoTranslationOptions(TranslationOptions):
    fields = ('nombre', 'descripcion')

@register(Miembro)
class MiembroTranslationOptions(TranslationOptions):
    fields = ('descripcion', 'descripcion_corta',)

@register(Servicio)
class ServicioTranslationOptions(TranslationOptions):
    fields = ('nombre', 'descripcion')

@register(Partner)
class PartnerTranslationOptions(TranslationOptions):
    fields = ('descripcion',)

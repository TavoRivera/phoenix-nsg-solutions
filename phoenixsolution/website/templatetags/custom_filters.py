from django import template
import re

register = template.Library()

@register.filter
def format_phone(value):
    """Formatea un número de teléfono a (XXX) XXX-XXXX"""
    digits = re.sub(r'\D', '', str(value))  # Elimina caracteres no numéricos
    if len(digits) == 11:
        return f"({digits[1:4]}) {digits[4:7]}-{digits[7:]}"
    return value  # Si no tiene 10 dígitos, lo devuelve sin cambios

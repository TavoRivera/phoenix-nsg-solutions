from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Miembro, Puesto, Servicio, Partner, ImagenesDeComentario, Comentario
from django.views.decorators.csrf import csrf_exempt
from .templatetags.custom_filters import format_phone
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from django.utils.translation import get_language

# Función para obtener los campos traducidos según el idioma
def get_translated_fields(obj, idioma):
    translated_fields = {}
    for field in obj._meta.get_fields():
        if field.is_relation or field.many_to_many:  # Excluir relaciones o campos M2M
            continue
        field_name = field.name
        translated_name = f"{field_name}_{idioma}"  # Ej. "nombre_en" si el idioma es "en"
        translated_fields[field_name] = getattr(obj, translated_name, getattr(obj, field_name))
    return translated_fields

# Vista principal
@csrf_exempt
def index(request):
    # Obtener el idioma activo
    idioma = get_language()

    # Consultar los miembros y traducir los campos según el idioma
    miembros = Miembro.objects.filter(mostrar_en_inicio=1)
    for miembro in miembros:
        translated = get_translated_fields(miembro, idioma)
        miembro.nombre = translated.get('nombre', miembro.nombre)  # Usar el nombre traducido

    servicios = Servicio.objects.all()
    partners = Partner.objects.all()
    comentarios = Comentario.objects.filter(respuesta_a=None)
    respuestas = Comentario.objects.exclude(respuesta_a=None)
    puestos = Puesto.objects.exclude(nombre__in=['Propietario de la Compañía','Company Owner']) 

    # Traducir los servicios
    for servicio in servicios:
        translated = get_translated_fields(servicio, idioma)
        servicio.nombre = translated.get('nombre', servicio.nombre)

    # Traducir los partners
    for partner in partners:
        translated = get_translated_fields(partner, idioma)
        partner.nombre = translated.get('nombre', partner.nombre)

    for puesto in puestos:
        translated = get_translated_fields(puesto, idioma)
        puesto.nombre = translated.get('nombre', puesto.nombre)
    
    imagenes_de_comentarios = ImagenesDeComentario.objects.all()

    return render(request, 'website/index.html', {
        'miembros': miembros,
        'servicios': servicios,
        'partners': partners,
        'puestos':puestos,
        'comentarios':comentarios,
        'respuestas':respuestas,
        'imagenes_de_comentarios':imagenes_de_comentarios,
    })

# Vista de miembros
@csrf_exempt
def members(request):
    idioma = get_language()
    miembros_queryset = Miembro.objects.all().order_by('puesto__nivel')  # Sin la coma, ahora es un QuerySet válido
    miembros = []  # Lista para almacenar miembros con teléfono formateado

    for miembro in miembros_queryset:
        miembro.telefono = format_phone(miembro.telefono)  # Formateamos el teléfono
        translated = get_translated_fields(miembro, idioma)
        miembro.nombre = translated.get('nombre', miembro.nombre)  # Traducir nombre
        miembros.append(miembro)  # Guardamos el miembro modificado en la lista

    return render(request, "website/members.html", {
        "miembros": miembros,  # Pasamos la lista modificada
    })

# Vista de contacto
def contact(request):
    if request.method == 'POST':
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]
        subject = f"Nueva solicitud de {name} recibida desde el sitio web"

        # Depuración: Ver datos en consola
        print(f"📩 Nombre: {name}, Email: {email}, Mensaje: {message}")

        # Renderizar la plantilla del email
        template = render_to_string('website/email.html', {
            'name': name,
            'email': email,
            'phone': phone,
            'subject': subject,
            'message': message
        })

        try:
            emailSender = EmailMessage(
                subject,
                template,
                settings.EMAIL_HOST_USER,
                ['octavioriv02@gmail.com']
            )
            emailSender.content_subtype = 'html'
            emailSender.send()

            # Mensaje de éxito
            messages.success(request, 'Se ha enviado tu solicitud. Pronto nos pondremos en contacto contigo.')
        
        except Exception as e:
            # Mensaje de error
            messages.error(request, f'❌ Error al enviar el mensaje: {str(e)}')

        return redirect('index')

    return render(request, "website/index.html")

def comentarios(request):
    if request.method == 'POST':
        nombre = request.POST["nombre"]
        puesto = request.POST["puesto"]
        mensaje = request.POST["mensaje"]
        print(f"mensaje de {nombre} con puesto {puesto}: {mensaje}")

        return redirect('index')
    return render(request, "website/index.html")
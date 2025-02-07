from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Miembro, Puesto, Servicio, Partner
from django.views.decorators.csrf import csrf_exempt
from .templatetags.custom_filters import format_phone
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages

# Create your views here.
@csrf_exempt
def index(request):
    miembros = Miembro.objects.filter(mostrar_en_inicio=1)
    servicios = Servicio.objects.all()
    partners = Partner.objects.all()
    return render(request, 'website/index.html', {'miembros': miembros,'servicios':servicios,'partners':partners})
    # return render(request,"website/index.html")

@csrf_exempt
def members(request):
    miembros_queryset = Miembro.objects.all().order_by('puesto__nivel')  # Sin la coma, ahora es un QuerySet válido
    miembros = []  # Lista para almacenar miembros con teléfono formateado

    for miembro in miembros_queryset:
        miembro.telefono = format_phone(miembro.telefono)  # Formateamos el teléfono
        miembros.append(miembro)  # Guardamos el miembro modificado en la lista

    return render(request, "website/members.html", {
        "miembros": miembros,  # Pasamos la lista modificada
    })

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
            'phone':phone,
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




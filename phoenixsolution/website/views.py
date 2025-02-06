from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Miembro, Puesto, Servicio, Partner
from django.views.decorators.csrf import csrf_exempt
from .templatetags.custom_filters import format_phone


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
        message = request.POST["message"]

        # Depuración: Imprimir los datos en la consola del servidor
        print(f"📩 Nombre: {name}, Email: {email}, Mensaje: {message}")

        # Retornar un mensaje en la pantalla para confirmar
        return HttpResponse("Formulario enviado correctamente.")

    return render(request, "website/index.html")
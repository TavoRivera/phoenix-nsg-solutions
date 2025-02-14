from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name = "index"),
    path("members",views.members, name = "members"),
    path("contact",views.contact, name = "contact"),
    path("contact/", views.contact, name="contact"),
     path("comentarios/", views.comentarios, name="comentarios"),
]

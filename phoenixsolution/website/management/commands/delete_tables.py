from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Eliminar tablas específicas de la base de datos'

    def handle(self, *args, **kwargs):
        tables = ["Puestos", "Miembros"]  # Nombres de las tablas a eliminar
        with connection.cursor() as cursor:
            for table in tables:
                try:
                    cursor.execute(f"DROP TABLE IF EXISTS {table};")
                    self.stdout.write(self.style.SUCCESS(f"Tabla {table} eliminada exitosamente."))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error eliminando {table}: {e}"))

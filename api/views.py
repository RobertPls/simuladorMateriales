import json
from django.http import JsonResponse
from django.conf import settings
import os

def getData(request):
    # Ruta al archivo JSON
    file_path = os.path.join(settings.BASE_DIR, 'api', 'data', 'data.json')

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Estructura de respuesta
        response = {
            "success": True,
            "data": data
        }
    except FileNotFoundError:
        response = {
            "success": False,
            "message": "Archivo no encontrado"
        }
    except json.JSONDecodeError:
        response = {
            "success": False,
            "message": "Error al decodificar JSON"
        }

    return JsonResponse(response, safe=False)

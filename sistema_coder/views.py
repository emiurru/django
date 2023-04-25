from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context
from datetime import datetime

def saludar(request):
    saludo = 'Hola usuario nuevo'
    pagina_html = HttpResponse(saludo)
    return pagina_html

def saludar_fecha(request):
    hoy = datetime.now()
    saludo = f'Hola usuari@, hoy es: {hoy.day}/{hoy.month}/{hoy.year}'
    pagina_html = HttpResponse(saludo)
    return pagina_html

def saludar_usuario(request, nombre):
    texto = f'Hola, {nombre}'
    pagina_html = HttpResponse(texto)
    return pagina_html

"""def probando_template(request):

    miHtml = open("C:/Users/Emiliano Longcred/Documents/Coderhouse/Django/sistema_coder/sistema_coder/Plantillas/template1.html")
    plantilla = Template(miHtml(read()))

    miHtml.close()

    miContexto = Context()

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)
"""
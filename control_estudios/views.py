from django.shortcuts import render


def listar_estudiantes(request):
    contexto = {
        'estudiantes':[
            {'nombre': 'Emiliano', 'apellido': 'Urrutia'},
            {'nombre': 'Alejo Miguel', 'apellido': 'Poch'}
            ]
    }
    
    http_responde = render(
        request=request,
        template_name='control_estudios/lista_estudiantes.html',
        context=contexto,
    )
    return http_responde
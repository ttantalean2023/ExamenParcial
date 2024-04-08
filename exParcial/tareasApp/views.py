from django.shortcuts import render, redirect

tareas = []

def vista_principal(request):
    return render(request, 'vista_principal.html', {'tareas': tareas})

def nueva_tarea(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        fecha_fin = request.POST.get('fecha_fin')
        estado = request.POST.get('estado')
        responsable = request.POST.get('responsable')

        # Agregar la nueva tarea a la lista
        tareas.append({
            'nombre': nombre,
            'descripcion': descripcion,
            'fecha_fin': fecha_fin,
            'estado': estado,
            'responsable': responsable
        })

        # Redireccionar a la vista principal para mostrar la lista actualizada de tareas
        return redirect('vista_principal')

    return render(request, 'nueva_tarea.html')

from django.shortcuts import render, redirect, get_object_or_404
from .models import Plato
from .forms import PlatoForm

def lista_platos(request):
    platos = Plato.objects.all()
    return render(request, 'menu/lista.html', {'platos': platos})

def crear_plato(request):
    form = PlatoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_platos')
    return render(request, 'menu/formulario.html', {'form': form})

def editar_plato(request, id):
    plato = get_object_or_404(Plato, id=id)
    form = PlatoForm(request.POST or None, instance=plato)
    if form.is_valid():
        form.save()
        return redirect('lista_platos')
    return render(request, 'menu/formulario.html', {'form': form})

def eliminar_plato(request, id):
    plato = get_object_or_404(Plato, id=id)
    plato.delete()
    return redirect('lista_platos')

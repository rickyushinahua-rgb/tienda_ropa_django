from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria, Prenda
from .forms import CategoriaForm, PrendaForm
# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')


# CRUD CATEGORÍAS

def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/listar.html', {'categorias': categorias})


def crear_categoria(request):
    form = CategoriaForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('listar_categorias')

    return render(request, 'categorias/formulario.html', {'form': form})


def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    form = CategoriaForm(request.POST or None, request.FILES or None, instance=categoria)

    if form.is_valid():
        form.save()
        return redirect('listar_categorias')

    return render(request, 'categorias/formulario.html', {'form': form})


def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria.delete()
    return redirect('listar_categorias')


# CRUD PRENDAS

def listar_prendas(request):
    prendas = Prenda.objects.all()
    return render(request, 'prendas/listar.html', {'prendas': prendas})


def crear_prenda(request):
    form = PrendaForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('listar_prendas')

    return render(request, 'prendas/formulario.html', {'form': form})


def editar_prenda(request, id):
    prenda = get_object_or_404(Prenda, id=id)
    form = PrendaForm(request.POST or None, request.FILES or None, instance=prenda)

    if form.is_valid():
        form.save()
        return redirect('listar_prendas')

    return render(request, 'prendas/formulario.html', {'form': form})


def eliminar_prenda(request, id):
    prenda = get_object_or_404(Prenda, id=id)
    prenda.delete()
    return redirect('listar_prendas')
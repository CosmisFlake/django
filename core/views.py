from django.shortcuts import redirect, render, HttpResponse
from crud.models import Joyeria, Marca

# Create your views here.
def root(request):
    return redirect('/inicio/')

def inicio(request):
    return render(request,'core/inicio.html')

def nosotros(request):
    return render(request,'core/nosotros.html')

def contacto(request):
    return render(request,'core/contacto.html')

def servicios(request):
    return render(request,'core/servicios.html')

def catalogo(request):
    context = {'joyerias': Joyeria.objects.all(),'marcas': Marca.objects.all()}
    return render(request,'core/catalogo.html',context)

def catalogo_by_marca(request, marca):
    context = {'joyerias': Joyeria.objects.filter(marca = marca),'marcas': Marca.objects.all()}
    return render(request,'core/catalogo.html',context)

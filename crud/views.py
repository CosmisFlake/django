from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import *
from .forms import *

# Create your views here.
def root(request):
    return redirect('joyeria/')

def joyeria_lista(request):
    context = {'joyeria': Joyeria.objects.all()}
    return render(request,'crud/joyeria.html',context)

def joyeria_new(request):
    if request.method == 'POST':
        form = JoyeriaForm(request.POST, request.FILES)
        if form.is_valid():
            idJoyeria = form.cleaned_data.get('idJoyeria')
            name = form.cleaned_data.get('name')
            tipo = form.cleaned_data.get('tipo')
            marca = form.cleaned_data.get('marca')
            value = form.cleaned_data.get('value')
            stock = form.cleaned_data.get('stock')
            image = form.cleaned_data.get('image')
            obj = Joyeria.objects.create(
                idJoyeria = idJoyeria,
                name = name,
                tipo = tipo,
                marca = marca,
                value = value,
                stock = stock,
                image = image
            )
            obj.save()
            return redirect(reverse('joyeria')+ '?OK')
        else:
            return redirect(reverse('joyeria')+ '?FAIL')
    else:
        form = JoyeriaForm
    return render(request,'crud/joyeria-new.html',{'form':form})

def joyeria_update(request,joyeria_id):
    try:
        joyeria = Joyeria.objects.get(idJoyeria = joyeria_id)
        form = JoyeriaForm(instance=joyeria)

        if request.method == 'POST':
            form = JoyeriaForm(request.POST, request.FILES, instance=joyeria)
            if form.is_valid():
                form.save()
                return redirect(reverse('joyeria') + '?UPDATED')
            else:
                return redirect(reverse('joyeria-edit') + joyeria_id) 

        context = {'form':form}
        return render(request,'crud/joyeria-edit.html',context)
    except:
        return redirect(reverse('joyeria') + '?NO_EXISTS')


def joyeria_detail(request, joyeria_id):
    try:
        joyeria = Joyeria.objects.get(idJoyeria = joyeria_id)
        if joyeria:
            context = {'joyeria':joyeria}
            return render(request,'crud/joyeria-detail.html',context)
        else:
            return redirect(reverse('joyeria') + '?lala')
    except:
        return redirect(reverse('joyeria') + '?FAIL')
    

def joyeria_by_marca(request, marca):
    try:
        joyerias = Joyeria.objects.filter(marca=marca)
        if joyerias:
            context = {'joyerias':joyerias}
            return render(request,'crud/joyeria.html',context)
        else:
            return redirect(reverse('joyeria') + '?FAIL')
    except:
        return redirect(reverse('joyeria') + '?FAIL')
    

def joyeria_by_tipo(request, tipo):
    try:
        joyerias = Joyeria.objects.filter(tipo=tipo)
        if joyerias:
            context = {'joyerias':joyerias}
            return render(request,'crud/joyeria.html',context)
        else:
            return redirect(reverse('joyeria') + '?FAIL')
    except:
        return redirect(reverse('joyeria') + '?FAIL')
    
def joyeria_delete(request, joyeria_id):
    try:
        joyeria = Joyeria.objects.get(idJoyeria=joyeria_id)
        joyeria.delete()
        return redirect(reverse('joyeria') + '?DELETED')
    except:
        return redirect(reverse('joyeria') + '?FAIL')


# Create your views here.

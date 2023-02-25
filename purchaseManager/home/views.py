from django.shortcuts import render, redirect
from .forms import DepForm
from .models import Depense


# Create your views here.

def index(request):
    depenses = Depense.objects.all()
    return render(request, 'index.html', {'depenses': depenses})


def create(request):

    if request.method == 'POST':
        dep = DepForm(request.POST).save()
        return redirect('./')

    else:
        dep = DepForm()

    return render(request, 'create.html', {'form': dep})

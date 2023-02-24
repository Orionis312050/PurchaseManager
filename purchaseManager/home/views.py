from django.shortcuts import render
from .forms import DepForm
from .models import Depense


# Create your views here.

def index(request):
    depenses = Depense.objects.all()
    return render(request, 'index.html', {'depenses': depenses})


def create(request):
    dep = DepForm()

    if dep.is_valid():
        title = dep.cleaned_data('title')
        desc = dep.cleaned_data('desc')
        quantity = dep.cleaned_data('quantity')
        depense = Depense(request.POST)
        depense.save()

    return render(request, 'create.html', {'form': dep})

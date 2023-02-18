from django.shortcuts import render
from .forms import ArtForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def create(request):
    art = ArtForm()
    return render(request, 'create.html', {'form':art})
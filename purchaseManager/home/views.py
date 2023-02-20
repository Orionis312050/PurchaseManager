from django.shortcuts import render
from .forms import ArtForm
from .models import Article


# Create your views here.

def index(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles': articles})


def create(request):
    art = ArtForm()

    if art.is_valid():
        title = art.cleaned_data('title')
        desc = art.cleaned_data('desc')
        auth = art.cleaned_data('auth')
        article = Article(request.POST)
        article.save()

    return render(request, 'create.html', {'form': art})

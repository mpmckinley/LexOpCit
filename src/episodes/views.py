from multiprocessing import context
from django.shortcuts import render
from .models import Ephemera, Episode, Book, Mentions

# Create your views here.
def book_library(request):
    library_queryset = Book.objects.all().order_by('author')
    episode_queryset = Episode.objects.select_related('ment_book')
    mention_queryset = Mentions.objects.select_related('ment_ep')
    context = {
        'books': library_queryset,
        'episodes': episode_queryset,
        'mentions': mention_queryset,
        'title': '- Library'
    }
    return render(request, "book/library.html", context)

def book_detail(request, pk):
    queryset = Book.objects.get(isbin=pk)
    context = {
        'book': queryset,
        'title': '- Books'
    } 
    return render(request, "book/book_detail.html", context)

def episode_library(request):
    queryset = Episode.objects.all()
    context = {
        'episodes': queryset,
        'title': "- Episodes"
    }
    return render (request, "episode/library.html", context)

def episode_detail(request, pk):
    queryset = Episode.objects.get(pk=pk)
    context = {
        'episode': queryset,
        'title': '- Episodes'
    }
    return render(request, "episode/episode_detail.html", context)
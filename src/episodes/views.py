# from multiprocessing import context
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.db.models import Count
from .models import Ephemera, Episode, Book, Mentions
from django.core.paginator import Paginator

from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
# from django_tables2 import SingleTableView

from .filters import BookFilter, EpisodeFilter#, EphemeraFilter
from .tables import BookTable, EpisodeTable

# Create your views here.

class FilteredBooksListView(SingleTableMixin, FilterView):
    table = BookTable
    model = Book
    queryset = Book.objects.all().order_by('author')
    template_name = "book/library.html"
    filterset_class = BookFilter


# def book_library(request):
#     library_queryset = Book.objects.all().order_by('author')
#     episode_queryset = Episode.objects.select_related('ment_book')
#     mention_queryset = Mentions.objects.select_related('ment_ep')
#     context = {
#         'books': library_queryset,
#         'episodes': episode_queryset,
#         'mentions': mention_queryset,
#         'title': '- Library'
#     }
#     return render(request, "book/library.html", context)

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

def ephemera_view(request):
    ephemera = Ephemera.objects.all().order_by('eph_ep')
    context = {
        'ephemera': ephemera,
    }
    return render (request, "ephemera.html", context)


class FilteredEphemeraListView(SingleTableMixin, FilterView):
    table = EpisodeTable
    model = Episode
    # Since we are particular about ephemera and only getting it through episodes,
    # we filter through episodes that have ephemera 
    queryset = Episode.objects.annotate(eph_count=Count('ephemera')).filter(eph_count__gt=0).order_by('-date')  
    template_name = "ephemera_filter.html"
    filterset_class = EpisodeFilter




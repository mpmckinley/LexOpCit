from itertools import groupby
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from episodes.models import Episode, Mentions, Ephemera

# Create your views here.
def home_view(request):
    episode_queryset = Episode.objects.all().order_by('-date')
    mention_queryset = Mentions.objects.select_related('ment_ep')
    context = {
        'episodes': episode_queryset,
        'mentions': mention_queryset,
    }
    # print(mention_queryset.query)
    # print(mention_queryset.query)
    return render(request, 'home.html', context)

def about_view(request, *args, **kwargs):
    context = {
        "title": "- About",
    }
    return render(request, 'about.html', context)

def ephemera_view(request):
    ephemera = Ephemera.objects.all().order_by('eph_ep')
    context = {
        'ephemera': ephemera,
    }
    return render (request, "ephemera.html", context)
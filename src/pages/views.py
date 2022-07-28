from itertools import groupby
from multiprocessing import context
from unittest import result
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from episodes.models import Episode, Mentions, Ephemera

# Create your views here.
def home_view(request):
    try:
        page = int(request.GET.get('page'))
    except:
        page = 1
    end = settings.PAGINATION_SIZE
    start = int((page - 1) * end)
    end *= page
    episode_queryset = Episode.objects.prefetch_related('mentions_set').all().order_by('-date')[start:end]
    context = {
        'episodes': episode_queryset,
        'page_number':page,
        'apply_infinite_scroll': 'yes'
    }
    # print(mention_queryset.query)
    # print(mention_queryset.query)
    return render(request, 'home.html', context)

def search_view(request):
    phrase =  request.GET.get('q')
    title_qs = Episode.objects.prefetch_related('mentions_set').filter(
        title__icontains=phrase)
    guest1_qs = Episode.objects.prefetch_related('mentions_set').filter(
        guest1__icontains=phrase)
    number_qs = Episode.objects.prefetch_related('mentions_set').filter(
        number__iexact=phrase)
    episode_queryset = (title_qs | guest1_qs | number_qs).distinct().order_by('-date')
    context = {
        'episodes': episode_queryset,
    }
    return render(request, 'home.html', context)

def about_view(request, *args, **kwargs):
    context = {
        # "title": "- About",
    }
    return render(request, 'about.html', context)


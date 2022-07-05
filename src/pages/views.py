from itertools import groupby
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from episodes.models import Episode, Mentions, Ephemera

# Create your views here.
def home_view(request):
    episode_queryset = Episode.objects.prefetch_related('mentions_set').all().order_by('-date')
    context = {
        'episodes': episode_queryset,
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
    episode_queryset = (title_qs | guest1_qs).distinct().order_by('-date')
    context = {
        'episodes': episode_queryset,
    }
    return render(request, 'home.html', context)

def about_view(request, *args, **kwargs):
    context = {
        "title": "- About",
    }
    return render(request, 'about.html', context)


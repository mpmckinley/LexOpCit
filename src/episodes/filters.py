import django_filters
from .models import Book, Ephemera, Episode

class BookFilter(django_filters.FilterSet):
    # isbin1 = django_filters.CharFilter(lookup_expr='iexact')
    # isbin2 = django_filters.CharFilter(lookup_expr='iexact')
    title = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Book
        fields = ['title', 'author']


class EphemeraFilter(django_filters.FilterSet):
    class Meta:
        model = Ephemera
        fields = ['film', 'paper', 'podcast', 'music', 'video', 'games', 'art', 'link']


class EpisodeFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Episode
        fields = ['title']
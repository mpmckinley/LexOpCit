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
    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
            super(BookFilter, self).__init__(data=data, queryset=queryset, request=request, prefix=prefix)
            self.filters['title'].field.widget.attrs.update({'class': 'form-control', 'placeholder': 'Title'})
            self.filters['author'].field.widget.attrs.update({'class': 'form-control', 'placeholder': 'Author'})


class EphemeraFilter(django_filters.FilterSet):
    class Meta:
        model = Ephemera
        fields = ['film', 'paper', 'podcast', 'music', 'video', 'games', 'art', 'link']


class EpisodeFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Episode
        fields = ['title']
    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
                super(EpisodeFilter, self).__init__(data=data, queryset=queryset, request=request, prefix=prefix)
                self.filters['title'].field.widget.attrs.update({'class': 'form-control', 'placeholder': 'Text Only'})


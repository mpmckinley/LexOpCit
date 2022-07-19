import django_filters
from .models import Book, Ephemera, Episode
from django.db.models import Q


class BookFilter(django_filters.FilterSet):

    # isbin1 = django_filters.CharFilter(lookup_expr='iexact')
    # isbin2 = django_filters.CharFilter(lookup_expr='iexact')
    # title = django_filters.CharFilter(lookup_expr='icontains')
    # author = django_filters.CharFilter(lookup_expr='icontains')
    title_author = django_filters.CharFilter(method='my_custom_filter',label="Search")

    class Meta:
        model = Book
        fields = ['title_author']
        
    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
            super(BookFilter, self).__init__(data=data, queryset=queryset, request=request, prefix=prefix)
            self.filters['title_author'].field.widget.attrs.update({'class': 'form-control', 'placeholder': 'Title or Author'})

    def my_custom_filter(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) | Q(author__icontains=value)
        )
    



class EphemeraFilter(django_filters.FilterSet):
    class Meta:
        model = Ephemera
        fields = ['film', 'paper', 'podcast', 'music', 'video', 'games', 'art', 'link']


class EpisodeFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(method='my_custom_filter',label="Search")
    class Meta:
        model = Episode
        fields = ['title']
    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
                super(EpisodeFilter, self).__init__(data=data, queryset=queryset, request=request, prefix=prefix)
                self.filters['title'].field.widget.attrs.update({'class': 'form-control', 'placeholder': 'Episode details'})

    def my_custom_filter(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) | Q(guest1__icontains=value) | Q(guest2__icontains=value)| Q(number__icontains=value)
        )


import django_tables2 as tables
from .models import Book, Ephemera, Episode
from django.core.paginator import Paginator

Table = tables.Table


def custom_paginate(self, paginator_class=Paginator, per_page=None, page=1, *args, **kwargs):
    """
    Paginates the table using a paginator and creates a ``page`` property
    containing information for the current page.
    """
    per_page = 12
    self.paginator = paginator_class(self.rows, per_page, *args, **kwargs)
    self.page = self.paginator.page(page)

    return self

Table.paginate = custom_paginate


class BookTable(Table):
    class Meta:
        model = Book
        template_name = "django_tables2/bootstrap.html"
        fields = ('title', )




class EphemeraTable(Table):
    class Meta:
        model = Ephemera
        template_name = "django_tables2/bootstrap.html"
        fields = ['film', 'paper', 'podcast', 'music', 'video', 'games', 'art', 'link']


class EpisodeTable(Table):
    class Meta:
        model = Episode
        template_name = "django_tables2/bootstrap4.html"
        fields = ['title']
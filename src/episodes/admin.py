from django.contrib import admin
from .models import Book, Episode, Mentions

# Register your models here.
admin.site.register(Episode)
admin.site.register(Book)
admin.site.register(Mentions)
from django.contrib import admin
from .models import Book, Ephemera, Episode, Mentions

# Register your models here.
admin.site.register(Episode)
admin.site.register(Book)
admin.site.register(Mentions)

# class EphemeraAdmin(admin.ModelAdmin)
#     list_display = ('eph_ep', 'film', 'paper', 'podcast', 'music', 'video', 'games', 'art', 'link')
admin.site.register(Ephemera)
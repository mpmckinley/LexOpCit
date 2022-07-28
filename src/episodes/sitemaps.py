import datetime
from django.conf import settings
from django.contrib import sitemaps
from django.shortcuts import reverse
from django.core.paginator import Paginator
from .models import *

class StaticViewsSitemap(sitemaps.Sitemap):

    priority = .8
    changefreq = "daily"

    def items(self):
        return [
            'about',
        ]
    
    def location(self, item):
        return reverse(item)
    
    def lastmod(self, obj):
        return datetime.datetime.now()


class EpisodeSitemap(sitemaps.Sitemap):

    changefreq = "daily"
    priority = 1.0

    def items(self):
        objects = Episode.objects.all()
        paginator = Paginator(objects, settings.PAGINATION_SIZE)
        return paginator.page_range
    
    def location(self, page_no):
        return "/?page="+str(page_no)

    def lastmod(self, obj):
        return datetime.datetime.now()


class EphemeraSitemap(sitemaps.Sitemap):

    changefreq = "daily"
    priority = .8

    def items(self):
        objects = Ephemera.objects.all()
        paginator = Paginator(objects, settings.LIBRARY_EPHEMERA_PAGINATION_SIZE)
        return paginator.page_range
    
    def location(self, page_no):
        return "/ephemera/?page="+str(page_no)
    
    def lastmod(self, obj):
        return datetime.datetime.now()
    

class BookSitemap(sitemaps.Sitemap):

    changefreq = "daily"
    priority = 0.8

    def items(self):
        objects = Book.objects.all()
        paginator = Paginator(objects, settings.LIBRARY_EPHEMERA_PAGINATION_SIZE)
        return paginator.page_range
    
    def location(self, page_no):
        return "/library/?page="+str(page_no)
    
    def lastmod(self, obj):
        return datetime.datetime.now()


class MentionsSitemap(sitemaps.Sitemap):

    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Episode.objects.all()

    def location(self, data):
        guest = data.guest1
        guest = guest.replace(" ", "%20")
        return "/episode_search?q="+str(guest)
    
    def lastmod(self, obj):
        return datetime.datetime.now()
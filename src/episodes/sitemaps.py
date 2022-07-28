from distutils.util import change_root
from django.conf import settings
from django.contrib import sitemaps
from django.shortcuts import reverse
from django.core.paginator import Paginator
from .urls import app_name
from .models import *

class StaticViewsSitemap(sitemaps.Sitemap):

    priority = 0.5
    changefreq = "daily"

    def items(self):
        return [
            'about',
        ]
    
    def location(self, item):
        return reverse(item)

class EpisodeSitemap(sitemaps.Sitemap):

    changefreq = "daily"
    priority = 0.5

    def items(self):
        objects = Episode.objects.all()
        paginator = Paginator(objects, settings.PAGINATION_SIZE)
        return paginator.page_range

    # def lastmod(self, obj):
    #     return obj.episode_number
    
    def location(self, page_no):
        return "/?page="+str(page_no)

    
    # def location(self, obj):
    #     return '/Episode' % (obj.episode_number)

# class BookSitemap(sitemaps.Sitemap):

#     changefreq = "daily"
#     priority = 0.5

#     def items(self):
#         return  Book.objects.all()
    
#     def lastmod(self, obj):
#         return obj.book_title
    
#     def location(self, obj):
#         return '/Book' % (obj.book_title)
        
# class MentionsSitemap(sitemaps.Sitemap):

#     changefreq = "daily"
#     priority = 0.5

#     def items(self):
#         return  Mentions.objects.all()
    
#     def lastmod(self, obj):
#         return obj.mentions_ment_ep
    
#     def location(self, obj):
#         return '/Mentions' % (obj.mentions_ment_ep)

# class EphemeraSitemap(sitemaps.Sitemap):

#     changefreq = "daily"
#     priority = 0.5

#     def items(self):
#         return  Ephemera.objects.all()
    
#     def lastmod(self, obj):
#         return obj.ephemera.eph_ep
    
#     def location(self, obj):
#         return '/Ephemera' % (obj.ephemera.eph_ep )

        
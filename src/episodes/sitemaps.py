from distutils.util import change_root
from django.contrib import sitemaps
from django.shortcuts import reverse
# from lexbooks.urls import *

class StaticViewsSitemap(sitemaps.Sitemap):

    priority = 0.5
    changefreq = "daily"

    def items(self):
        return [
            'about',
            'home',
            'episode-search',
            'books',
            'episodes',
            'ephemera',
        ]
    
    def location(self, item):
        return reverse(item)
        
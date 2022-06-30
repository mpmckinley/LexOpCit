from datetime import date
from inspect import isbuiltin
from pickle import TRUE, FALSE
from django.db import models

class Episode(models.Model):
    number      = models.IntegerField()
    title       = models.CharField(max_length=120)
    guest1      = models.TextField()
    guest2      = models.TextField(blank=TRUE)
    guest3      = models.TextField(blank=TRUE)
    guest4      = models.TextField(blank=TRUE)
    date        = models.DateField()
    yt_url      = models.TextField()
    tags        = models.TextField()

    def __str__(self):
        return f"{self.number}|{self.date} : {self.guest1} - {self.title}"

class Book(models.Model):
    isbin1      = models.CharField(max_length=13)
    isbin2      = models.CharField(max_length=13)
    title       = models.TextField()
    author      = models.TextField()
    amzn_url    = models.TextField()
    tb_url      = models.TextField(null=True, blank=True)
    image       = models.TextField()

    def __str__(self):
        return f"{self.id} : {self.title} - {self.author}"

class Mentions(models.Model):
    ment_ep     = models.ForeignKey(Episode, on_delete=models.CASCADE)
    ment_book   = models.ForeignKey(Book, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "mentions"

    def __str__(self):
        return f"{self.ment_ep} --- {self.ment_book}"

class Ephemera(models.Model):
    eph_ep      = models.ForeignKey(Episode, on_delete=models.CASCADE)
    film        = models.TextField(null=True, blank=True)
    paper       = models.TextField(null=True, blank=True)
    podcast     = models.TextField(null=True, blank=True)
    music       = models.TextField(null=True, blank=True)
    video       = models.TextField(null=True, blank=True)
    games       = models.TextField(null=True, blank=True)
    art         = models.TextField(null=True, blank=True)
    link        = models.TextField()
    class Meta:
        verbose_name_plural = "ephemera"


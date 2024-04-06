from unicodedata import category
from django.db import models
from numpy import product
# Static-Pages.
class StaticPosts(models.Model):
    title = models.CharField(max_length=160)
    page_name = models.CharField(max_length=70)
    content = models.TextField()
    slug = models.CharField(max_length=70, unique=True)

    def __str__(self):
        return self.title

class PatreonImage(models.Model):
    image = models.ImageField(upload_to='patreon_logos')

# Site-Data.
class SiteData(models.Model):
    email = models.CharField(max_length=160, default="")
    phone =models.IntegerField(default=123456789)
    logo = models.ImageField(upload_to='logo',blank=True, null=True)
    favicon = models.ImageField(upload_to='logo',blank=True, null=True)
    facebook = models.CharField(max_length=160,  default="", blank=True, null=True)
    instagram = models.CharField(max_length=160,  default="", blank=True, null=True)
    twitter = models.CharField(max_length=160,default="", blank=True, null=True)
    youtube = models.CharField(max_length=160,default="", blank=True, null=True)
    address = models.CharField(max_length=260,default="")
    home_heading = models.CharField(max_length=160,default="")
    home_paragraph = models.CharField(max_length=160,default="")
    home_banner_img = models.ImageField(upload_to='home_banner',blank=True, null=True)
    home_logo = models.ManyToManyField(PatreonImage, blank=True, null=True)
    made_by = models.CharField(max_length=160,default="")
    copyright = models.CharField(max_length=160,default="")
    footer_large_text1 = models.CharField(max_length=160,default="")
    footer_large_text2 = models.CharField(max_length=160,default="")



class Faqs(models.Model):
    question = models.CharField(max_length=260)
    answer = models.TextField()

    def __str__(self):
        return self.question
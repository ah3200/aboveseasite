from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from taggit.managers import TaggableManager

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=40,unique=True,blank=True,null=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unicode(self.name))
        super(Category,self).save(*args,**kwargs)
        
    def get_absolute_url(self):
        return "/category/%s/" % (self.slug)
    
    def __unicode__(self):
        return self.name
        
    class Meta:
        verbose_name_plural = 'categories'

class Story(models.Model):
    
    STATUS_CHOICES = (
        ('D', 'Draft'),
        ('P', 'Published'),
    )
    DRAFT = 'D'
    PUBLISHED = 'P'

    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    text = models.TextField()
    slug = models.SlugField(max_length=40,unique=True)
    author = models.ForeignKey(User)
    pub_status = models.CharField(max_length=1,choices=STATUS_CHOICES,default=DRAFT)
    category = models.ForeignKey(Category,blank=True,null=True)
    tags = TaggableManager()

    def get_absolute_url(self):
        return "%s/%s/%s/" % (self.pub_date.year, self.pub_date.month, self.slug)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'stories'
        ordering = ["-pub_date"]


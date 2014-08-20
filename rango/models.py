from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	description = models.CharField(max_length=500, default="")

	def __unicode__(self):
		return self.name

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    bio = models.CharField(max_length=250, default="")
    location = models.CharField(max_length=100,  default="")
	
    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username


class Page(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=128)
	url = models.URLField()
	content = models.CharField(max_length=1000)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	drafter = models.ForeignKey(User, to_field='username')
	date = models.DateTimeField(default=datetime.now())
	
	def __unicode__(self):
		return self.title
		

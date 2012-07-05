from django.contrib import admin
from django.db import models

# Create your models here.
class Post(models.Model):
	title=models.CharField(max_length=60)
	body=models.TextField()
	created=models.DateField()
	updated=models.DateField()
	def __unicode__(self):
		return self.title
class Blog(models.Model):
	body=models.TextField()
	author=models.CharField(max_length=60)
	created=models.DateField()
	updated=models.DateField()
	post=models.ForeignKey(Post,related_name='Posts')

admin.site.register(Post)
admin.site.register(Blog)


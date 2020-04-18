from django.db import models

# Create your models here.

class post(models.Model):
	short_title = models.CharField(max_length=50)
	title = models.CharField(max_length=150)
	description = models.TextField(default="to be updated")
	use_case = models.TextField(default="to be updated")
	lang = models.CharField(max_length=50,default="VB.NET")
	version = models.IntegerField(default=2019)
	posted_on = models.DateTimeField(auto_now_add=True)
	video_id = models.CharField(max_length=70)
	source_code = models.URLField(max_length=200,blank=True)
	views = models.IntegerField(default=0,editable=False)
	meta_description = models.TextField(default="")
	meta_keyword = models.TextField(default="")
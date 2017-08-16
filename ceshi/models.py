from django.db import models

# Create your models here.

class Article(models.Model):
    '''
    文章内容表
    '''
    uid = models.CharField(max_length=108, primary_key=True)
    content = models.TextField(verbose_name="文章内容")

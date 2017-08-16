from django.contrib import admin
from ceshi import models
from pagedown.widgets import AdminPagedownWidget
from django import forms


# Register your models here.
# 定义自己的form
class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = models.Article
        fields = '__all__'


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm


# admin.site.register(models.Article)
admin.site.register(models.Article,ArticleAdmin)

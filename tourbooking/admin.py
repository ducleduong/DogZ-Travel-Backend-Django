from django.contrib import admin
from django import forms
from django.forms import widgets
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib.auth.models import Permission, Group


class CustomForm(forms.Form):
    content = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Tours
        fields = '__all__'

class ToursAdmin(admin.ModelAdmin):
    forms = CustomForm


admin.site.register(User)
admin.site.register(Location)
admin.site.register(CategoryTour)
admin.site.register(Tours,ToursAdmin)
admin.site.register(News)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(RatingTour)
admin.site.register(Permission)
admin.site.register(TourImages)


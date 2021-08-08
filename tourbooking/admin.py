from django.contrib import admin
from django import forms
from django.forms import widgets
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class CustomForm(forms.Form):
    content = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Travel
        felds = '__all__'

class TravelAdmin(admin.ModelAdmin):
    forms = CustomForm

admin.site.register(User)
admin.site.register(Location)
admin.site.register(CategoryHotel)
admin.site.register(CategoryTravel)
admin.site.register(Hotel)
admin.site.register(Travel,TravelAdmin)
admin.site.register(News)
admin.site.register(ImagesHotel)
admin.site.register(ImagesTravel)
admin.site.register(ReviewTravel)
admin.site.register(ReviewHotel)
admin.site.register(Comment)
admin.site.register(Provincial)
admin.site.register(District)
admin.site.register(Ward)



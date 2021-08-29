
from tour.views import CustomTokenView
from django.contrib import admin
from django.urls import path, include
from django.urls.conf import re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tourbooking.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    re_path(r'auth/token/$', CustomTokenView.as_view(), name="token"),
    path('auth/', include('oauth2_provider.urls',namespace='oauth2_provider'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

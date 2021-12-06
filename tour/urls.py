
from tour.views import CustomTokenView
from django.contrib import admin
from django.urls import path, include
from django.urls.conf import re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Tours API')


urlpatterns = [
    path('', schema_view),
    path('admin/', admin.site.urls),
    path('', include('tourbooking.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    re_path(r'auth/token/$', CustomTokenView.as_view(), name="token"),
    path('auth/', include('oauth2_provider.urls',namespace='oauth2_provider')),
    # re_path(r'^swagger(?P<format>\.json|\.yaml)$',schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

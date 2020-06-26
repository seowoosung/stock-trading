from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('api.urls', namespace='api')),
]

if 'drf_yasg' in settings.INSTALLED_APPS:
    from rest_framework import permissions
    from drf_yasg.views import get_schema_view
    from drf_yasg import openapi

    schema_view = get_schema_view(
        openapi.Info(
            title="Stock trading API",
            default_version='v1',
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
    )

    urlpatterns = urlpatterns + [
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]

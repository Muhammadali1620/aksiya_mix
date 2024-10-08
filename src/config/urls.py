from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

from .yasg import schema_view

urlpatterns = [
    #Django
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),

    # Rest
    path('rest_api', include('rest_framework.urls')),

    # Swagger
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # My apps
    path('api/v1/discount/', include('apps.discounts.urls')),
    path('api/v1/auth/', include('apps.authentication.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

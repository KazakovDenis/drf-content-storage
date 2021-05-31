from django.contrib import admin

from django.urls import path, include

from core.views import index_view

urlpatterns = [
    path('', index_view, name='index'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('api.urls', namespace='api')),
]

from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# schema_view = get_schema_view(
#    openapi.Info(
#       title="TaskFlow API",
#       default_version='v1',
#       description="Task management API",
#    ),
#    public=True,
#    permission_classes=[permissions.AllowAny],
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),
    # path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
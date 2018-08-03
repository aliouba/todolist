from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'rest-auth/', include('rest_auth.urls')),
    path(r'', include('todo.urls')),
]

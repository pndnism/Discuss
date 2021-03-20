from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('discuss/', include('discuss_app.urls')),
    path('admin/', admin.site.urls),
]
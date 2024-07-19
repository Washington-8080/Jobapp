from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Jobapp1.urls')),  # Include Jobapp1's URLs
]

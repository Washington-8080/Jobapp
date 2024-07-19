from django.contrib import admin
from django.urls import path, include
from Jobapp1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('update/', views.update_user, name='update_user'),
    path('delete/', views.delete_user, name='delete_user'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('job/search/', views.job_search, name='job_search'),
    path('search/', views.search, name='search'),
    path('', views.home, name='home'),  # Root URL
]

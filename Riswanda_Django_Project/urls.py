from django.contrib import admin
from django.urls import path
from login import views as login_app

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('login/', login_app.login_page),
]

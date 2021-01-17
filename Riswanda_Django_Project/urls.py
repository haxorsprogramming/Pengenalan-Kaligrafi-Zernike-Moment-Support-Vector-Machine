from django.contrib import admin
from django.urls import path
from login import views as login_app
from home import views as home_app

urlpatterns = [
    path('', home_app.home_page),
    path('admin/', admin.site.urls),
    path('login/', login_app.login_page),
]

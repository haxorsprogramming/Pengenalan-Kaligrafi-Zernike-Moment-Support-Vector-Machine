from django.contrib import admin
from django.urls import path
from login import views as login_app
from home import views as home_app

urlpatterns = [
    path('', home_app.home_page),
    path('admin/', admin.site.urls),
    path('login/', login_app.login_page),
    path('login/proses', login_app.login_proses),
    path('test-rest/', home_app.test_rest),
    path('get/mahasiswa/all', home_app.mahasiswa_all)
]

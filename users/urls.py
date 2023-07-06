from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('logout/', views.log_out, name='logout'),
]

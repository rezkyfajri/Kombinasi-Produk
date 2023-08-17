from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
         path('home/', views.home, name ='home'),
         path('upload/', views.upload, name ='upload'),
         path('train/', views.train, name ='train'),
]
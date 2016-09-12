from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
   url(r'^home2/', home , name = 'home'),
   url(r'^test/' , test , name = 'test')
]

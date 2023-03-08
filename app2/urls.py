from app2.views import *
from django.urls import path
app_name='Nothing'
urlpatterns = [
    path('Life1/',Life1,name='Life1'),
    path('life2/',life2,name='life2'),
]

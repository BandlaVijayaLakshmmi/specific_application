from app1.views import *
from django.urls import path
app_name='something'
urlpatterns = [
    path('life/',life,name='life'),
    path('abd/',abd,name='abd')
]

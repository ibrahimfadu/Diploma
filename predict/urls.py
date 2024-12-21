from . import views
from django.urls import path

app_name = 'predict'  

urlpatterns=[
    path("/cutoff",views.cutoff,name="cutoff")
]
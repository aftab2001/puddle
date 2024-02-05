from django.urls import path
from . import views

app_name='my_dashboard'
urlpatterns = [
    path('',views.index,name='index')
]
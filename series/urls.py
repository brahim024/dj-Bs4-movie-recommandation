from django.urls import path
from .import views

app_name='series'
urlpatterns=[
	path('',views.get_serie,name='get_serie'),
]
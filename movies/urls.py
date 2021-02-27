from django.urls import path
from .import views
from .views import Deletemovie
app_name='movies'
urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<pk>/',Deletemovie.as_view(),name='delete')
]

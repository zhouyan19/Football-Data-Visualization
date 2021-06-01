from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('delete/', views.delete_data, name='delete'),
    path('edit/', views.change, name='change'),
    path('query/', views.search, name='search'),
    path('getOne/', views.getOne, name='getOne'),
    path('rank/', views.ranking_query_data, name='rank')
]
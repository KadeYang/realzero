from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ranking/', views.ranking, name='ranking'),
    path('community/', views.community, name='community'),
    path('search/', views.search, name='search'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    
    
]

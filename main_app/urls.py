from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('deals/', views.deal_index, name='deal_index'),
    path('deals/<int:deal_id>/', views.deal_detail, name='deal-detail'),


]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('deals/', views.deal_index, name='deal-index'),
    path('deals/<int:deal_id>/', views.deal_detail, name='deal-detail'),
    path('deals/create/', views.DealCreate.as_view(), name='deal-create'),
    path('deals/<int:pk>/update/', views.DealUpdate.as_view(), name='deal-update'),
    path('deals/<int:pk>/delete/', views.DealDelete.as_view(), name='deal-delete'),
]

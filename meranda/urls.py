from django.urls import path
from . import views


urlpatterns = [
    path('', views.CategoryListView.as_view(), name='category-list'),
    path('healthy/', views.HealthyListView.as_view(), name='healthy-list'),
    path('healthy/<int:pk>/', views.HealthyDetailView.as_view(), name='healthy-detail'),
    path('sport/', views.SportListView.as_view(), name='sport-list'),
    path('sport/<int:pk>/', views.SportDetailView.as_view(), name='sport-detail'),
    path('design/', views.DesignListView.as_view(), name='design-list'),
    path('design/<int:pk>/', views.DesignDetailView.as_view(), name='design-detail'),
    path('contact/',views.contact_view, name='index'),
    path('contact/success/', views.contact_success_view, name='success'),
    
    

]

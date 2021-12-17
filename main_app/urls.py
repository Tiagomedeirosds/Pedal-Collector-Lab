from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pedals/', views.pedals_index, name='index'),
    path('pedals/<int:pedal_id>/', views.pedals_detail, name='detail'),
    path('pedals/create/', views.PedalCreate.as_view(), name='pedals_create'),
    path('pedals/<int:pk>/update/', views.PedalUpdate.as_view(), name='pedals_update'),
    path('pedals/<int:pk>/delete/', views.PedalDelete.as_view(), name='pedals_delete'),
    path('pedals/<int:pedal_id>/add_checked/', views.add_checked, name='add_checked'),
    path('pedals/<int:pedal_id>/assoc_guitar/<int:guitar_id>/', views.assoc_guitar, name='assoc_guitar'),

    path('pedals/<int:pedal_id>/unassoc_guitar/<int:guitar_id>/', views.unassoc_guitar, name='unassoc_guitar'),

    path('guitars/', views.GuitarList.as_view(), name='guitars_index'),
    path('guitars/<int:pk>/', views.GuitarDetail.as_view(), name='guitars_detail'),
    path('guitars/create/', views.GuitarCreate.as_view(), name='guitars_create'),
    path('guitars/<int:pk>/update/', views.GuitarUpdate.as_view(), name='guitars_update'),
    path('guitars/<int:pk>/delete/', views.GuitarDelete.as_view(), name='guitars_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    


]
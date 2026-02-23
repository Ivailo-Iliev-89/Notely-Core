from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('note/<int:note_id>/pin/', views.toggle_pin, name='toggle_pin'),
]

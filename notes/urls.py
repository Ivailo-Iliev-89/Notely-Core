from django.urls import path
from . import views

urlpatterns = [
    path('', views.NoteListView.as_view(), name='note_List'),
    path('create/', views.NoteListView.as_view(), name='note-create'),
    path('<int:pk>/', views.NoteListView.as_view(), name='note-detail'),
    path('<int:pk>/edit/', views.NoteListView.as_view(), name='note-edit'),
    path('int:pk>/delete/', views.NoteListView.as_view(), name='note-delete'),
]

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from notes.views import NoteViewSet

router = DefaultRouter()
router.register(r'notes-api', NoteViewSet, basename='note-api')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Login/Logout/Password
    path('notes/', include('notes.urls')),  # CRUD
    path('api/', include(router.urls)),
    # path('tags/', include('tags.urls')),  # tasks
]

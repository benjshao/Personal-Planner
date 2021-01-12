from django.urls import path
from . import views
from .views import TaskDetailView, TaskDeleteView

urlpatterns = [
    path('', views.home, name='todolist-home'),
    path('dashboard/', views.list, name="todolist-list"),
    path('about/', views.about, name='todolist-about'),
    path('item/<int:pk>/', TaskDetailView.as_view(), name='todolist-detail'),
    path('item/<int:pk>/delete', TaskDeleteView.as_view(), name='todolist-delete')
]
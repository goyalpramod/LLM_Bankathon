from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard_view'),
    path('create/', views.create_job, name='create_job'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('cvDashboard/', views.cv_page, name='cv_page'),
]

from django.urls import path
from . import views


app_name = 'cvDashboard'

urlpatterns = [
    path('cvDashboard/', views.cv_page, name='cv_page'),
    path('job/', views.cv_page, name='cv_page'),
    path('list/', views.upload_file, name='cv_name'),
]

from django.contrib import admin
from django.urls import path,include
from LandingPage.views import landing_page
from cvDashboard.views import upload_file

urlpatterns = [
    path('', landing_page, name="landing_page"),
    path('accounts/', include('accounts.urls')),
    path('', include('dashboard.urls')),
    path('', include('cvDashboard.urls')),
    path('list/', upload_file, name='list'),
]

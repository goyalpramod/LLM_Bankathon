from django.contrib import admin
from django.urls import path,include
from LandingPage.views import landing_page

urlpatterns = [
    path('', landing_page, name="landing_page"),
    path('accounts/', include('accounts.urls')),
    path('', include('dashboard.urls')),
]

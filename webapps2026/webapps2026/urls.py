from django.urls import path, include

urlpatterns = [
    path('webapps2026/', include('register.urls')),
    path('webapps2026/', include('payapp.urls')),
    path('webapps2026/', include('conversionservice.urls')),
]
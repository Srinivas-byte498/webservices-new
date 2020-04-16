"""webservices URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Savart API')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/',include('personal_profile.urls')),
    path('clients/',include('subscriptions.urls')),
    path('clients/',include('registration.urls')),
    path('clients/',include('investment_profile.urls')),
    path('clients/',include('customer.urls')),
    path('ui/',include('webapp.urls')),
    path('public/',include('metadata.urls')),
    path(r'swagger', schema_view),
]

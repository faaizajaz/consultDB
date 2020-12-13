"""opmconsultdb URL Configuration

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
import query.views as QueryViews
import rating.views as RatingViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', QueryViews.ConsultantQueryView, name='consultant-query'),
    path('consultant/', include('consultant.urls')),
    path('ratingsearch/', RatingViews.RatingSearchView, name='rating-search')
]

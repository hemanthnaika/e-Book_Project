"""
URL configuration for eBooks_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

# All the url are handle in this section
urlpatterns = [
    path('admin/', admin.site.urls),
    # Add the home page url by creating new file urls.py in eBook_app file  by adding folder name.file name
    path('', include('eBook_app.urls')),
    # '' means home page. include means add eBook-app urls
]

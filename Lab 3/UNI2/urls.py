"""
URL configuration for UNI2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
# UNI2/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from students.views import StudentViewSet
from instructors.views import InstructorViewSet
from courses.views import CourseViewSet
from django.views.generic import RedirectView

router = DefaultRouter()
router.register('students', StudentViewSet)
router.register('instructors', InstructorViewSet)
router.register('courses', CourseViewSet)

urlpatterns = [
    path('', RedirectView.as_view(url='/api/')),
    path('api/', include(router.urls)),
]
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
    path('courses/', include('courses.urls')),
    path('instructor/', include('instructor.urls')),
    path('', lambda request: redirect('instructor/')),
]
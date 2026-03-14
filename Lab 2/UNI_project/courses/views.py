from django.shortcuts import render, get_object_or_404
from .models import Course


def course_list(request):
    courses = Course.objects.prefetch_related('students').all()
    return render(request, 'course_list.html', {'courses': courses})


def course_detail(request, pk):
    course = get_object_or_404(
        Course.objects.prefetch_related('students').select_related('instructors'),
        pk=pk
    )
    return render(request, 'course_detail.html', {'course': course})
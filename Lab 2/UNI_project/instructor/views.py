from django.shortcuts import render, get_object_or_404
from .models import Instructor


def instructor_list(request):
    instructors = Instructor.objects.select_related('courses').all()
    return render(request, 'instructor_list.html', {'instructors': instructors})


def instructor_detail(request, pk):
    instructor = get_object_or_404(
        Instructor.objects.select_related('courses').prefetch_related('courses__students'),
        pk=pk
    )
    return render(request, 'instructor_detail.html', {'instructor': instructor})
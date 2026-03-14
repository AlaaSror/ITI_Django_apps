from django.shortcuts import render, get_object_or_404
from .models import Student


def student_list(request):
    students = Student.objects.prefetch_related('courses').all()
    return render(request, 'student_list.html', {'students': students})


def student_detail(request, pk):
    student = get_object_or_404(
        Student.objects.prefetch_related('courses__instructors'),
        pk=pk
    )
    return render(request, 'student_detail.html', {'student': student})
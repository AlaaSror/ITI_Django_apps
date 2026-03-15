from rest_framework import viewsets
from .models import Course
from .serializers import CourseSerializer, CourseCreateUpdateSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().select_related('instructor').prefetch_related('students')

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CourseCreateUpdateSerializer
        return CourseSerializer
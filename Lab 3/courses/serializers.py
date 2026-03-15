from rest_framework import serializers
from .models import Course
from students.serializers import StudentSerializer
from instructors.serializers import InstructorSerializer
from students.models import Student
from instructors.models import Instructor

# read the courses (all nested object in it)
class CourseSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True)
    instructors = InstructorSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['name', 'code', 'students', 'instructors']

# write the courses (with the nested object in it)
class CourseCreateUpdateSerializer(serializers.ModelSerializer):
    instuctor_id = serializers.PrimaryKeyRelatedField(queryset=Instructor.objects.all(), source='instructor')
    student_ids = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), many=True, source='students')

    class Meta:
        model = Course
        fields = ['name', 'code', 'students', 'instructor']
    # create validation over the course data
    def create(self, validated_data):
        students = validated_data.pop('students', [])
        instructor = validated_data.pop('instructor', None)
        course = Course.objects.create(**validated_data)
        if instructor:
            course.instructor = instructor
            course.save()
        if students:
            course.students.set(students)
        return course
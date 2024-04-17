from django.shortcuts import render
from django.views import View
from .models import Course, Teacher



class CourseView(View):
    def get(self, request):
        courses = Course.objects.all()
        context = {
            'courses': courses,
        }
        return render(request, 'main/course.html', context)


class TeacherView(View):
    def get(self, request):
        teachers = Teacher.objects.all()
        context = {
            'teachers': teachers,
        }
        return render(request, 'main/teacher.html', context)

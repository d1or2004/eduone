from django.urls import path
from .views import TeacherView, CourseView

urlpatterns = [
    path('teachers', TeacherView.as_view(), name='teachers'),
    path('courses/', CourseView.as_view(), name='courses'),
]

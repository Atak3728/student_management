from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, CourseViewSet, AttendanceViewSet

router = DefaultRouter()
router.register('students', StudentViewSet)
router.register('courses', CourseViewSet)
router.register('attendance', AttendanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

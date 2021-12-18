from django.urls import path

from . import views

app_name = "courses"

urlpatterns = [
    path('', views.CourseListView.as_view(), name='course_list'),
    path('<pk>/<slug>/', views.CourseDetailView.as_view(), name='course_detail'),
    path('<int:course_id>/<pk>/<slug>/', views.LessonView.as_view(), name='lesson_detail'),
]

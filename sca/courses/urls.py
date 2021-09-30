from django.urls import path

from . import views

app_name = "courses"

urlpatterns = [
    path("", views.CourseListView.as_view(), name="list"),
    path("<pk>/<slug:slug>/", views.CourseDetailView.as_view(), name="detail"),
    path("<int:c_id>/<slug:c_slug>/lessons/<pk>/<slug:slug>",
        views.LessonDetailView.as_view(), name="lesson_detail"),
]

from django.urls import path

from . import views

app_name = "courses"

urlpatterns = [
    path('<int:c_id>/buy_course/', views.buy_course, name="buy_course"),
    path("<pk>/<slug:slug>/", views.CourseDetailView.as_view(), name="detail"),
    path("<int:c_id>/<slug:c_slug>/lessons/<pk>/<slug:slug>",
         views.LessonDetailView.as_view(), name="lesson_detail"),
    path("", views.CourseListView.as_view(), name="list"),

]

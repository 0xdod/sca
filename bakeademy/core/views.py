from django.shortcuts import render

from ..courses.models import Course


# Create your views here.


def index_page(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses': courses})

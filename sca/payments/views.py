import string
import random

from django.shortcuts import get_object_or_404, render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required


from sca.courses.models import Course
# from rave_python import Rave


# rave = Rave(settings.RAVE_PUBLIC_KEY)

def gen_random_str(limit=10):
    return "".join(random.choices(string.ascii_letters+string.digits, k=limit))


# Create your views here.

@login_required
def process_payments(request):

    payment_info = request.session.get('payment_info')
    course = get_object_or_404(Course, pk=payment_info['course_id'])
    context = {
        'tx_ref': gen_random_str(),
        'public_key': settings.RAVE_PUBLIC_KEY,
        'course': course,
        'payment_info': payment_info}

    return render(request, 'payments/process.html', context)


def callback(request):
    status = request.GET.get('status')
    redirect_url = ''
    if status == 'successful':
        redirect_url = 'payments:success'
    else:
        redirect_url = 'payments:cancelled'

    return redirect(redirect_url)


def payment_cancelled(request):
    context = {}
    return render(request, 'payments/cancelled.html', context)


def payment_success(request):

    payment_info = request.session.get('payment_info')
    course = get_object_or_404(Course, pk=payment_info['course_id'])
    user = request.user
    user.enroll(course)
    context = {}

    return render(request, 'payments/success.html', context)

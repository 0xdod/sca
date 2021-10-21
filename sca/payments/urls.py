from django.urls import path

from . import views


app_name = 'payments'

urlpatterns = [
    path('process/', views.process_payments, name='process'),
    path('callback/', views.callback, name="callback"),
    path('success/', views.payment_success, name="success"),
    path('cancelled/', views.payment_cancelled, name="cancelled"),
]
from django.urls import path
from django.conf.urls import url
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView

from .views import LoginView, PasswordView, RegisterView
from . import views

urlpatterns = [

    path('login',LoginView.as_view(),name='login'),
    path('reset',PasswordView.as_view(), name='reset'),
    path('register',RegisterView.as_view(), name='register'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url('reset-password/',PasswordResetView.as_view(),name='reset_password'),
    url('reset-password-done/',PasswordResetDoneView.as_view(),name='reset_password-done'),
    url('reset-password-confirm/',PasswordResetDoneView.as_view(),name='reset_password-done'),
    url('reset-password-complete/',PasswordResetDoneView.as_view(),name='reset_password-done'),

]

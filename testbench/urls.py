from django.urls import path,include
from .views import test

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('test',test)
]
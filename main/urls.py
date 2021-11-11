from django.urls import path,include
from .views import home, download_file

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', home),
    path('download',download_file)
]
from django.urls import path, re_path
from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    #re_path(r'^(?P<slug>\w+)/$', views.ResultsView.as_view(), name='results'),
    path('<slug:slug>', views.ResultsView.as_view(), name='results'),
    path('entry', views.sheet_entry_view, name='entry'),
    path('edit/<slug:slug>', views.UpdateView.as_view(), name='update'),
]
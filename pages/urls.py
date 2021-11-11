from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.ResultsView.as_view(), name='results'),
    path('entry', views.sheet_entry_view, name='entry'),
    path('edit/<int:pk>', views.UpdateView.as_view(), name='update'),
]


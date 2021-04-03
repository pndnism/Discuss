from django.urls import path
from . import views

app_name = 'discuss'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:discuss_theme_id>/', views.detail, name='detail'),
    path('<int:discuss_theme_id>/entry/', views.entry, name='entry'),
    path('<int:discuss_theme_id>/waiting/', views.waiting, name='waiting'),
    path('<int:discuss_theme_id>/discussion/', views.discussion, name='discussion'),
]
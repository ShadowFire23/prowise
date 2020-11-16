from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('<str:url_sistem>/', views.event_detail, name='event-detail')
]

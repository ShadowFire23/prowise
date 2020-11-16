from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name="post_list"),
    path('<str:url_sistem>/', views.post_detail, name='post-detail'),
]

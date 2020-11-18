from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('support/',views.support_create,name='support'),
    path('contact/',views.contact_create,name='contact'),
    path('haberler/', views.new_list,name='news'),
]

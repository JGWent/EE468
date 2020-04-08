from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_name, name='get_name'),
    path('admin_page', views.admin_page, name='admin'),
    path('show', views.show, name='show'),
]


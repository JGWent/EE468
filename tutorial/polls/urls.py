from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_name, name='get_name'),
    path('logout', views.logout, name='logout'),
    path('admin_page', views.admin_page, name='admin'),
    path('prof_page', views.prof_page, name='prof'),
    path('Check', views.Check, name='check'),
    path('show', views.show, name='show'),
    path('semester', views.semester, name='semester'),
    path('results', views.results, name='results'),
    path('semester2', views.semester2, name='semester2'),
    path('results2', views.results2, name='results2'),
    path('student', views.student, name='student'),
]


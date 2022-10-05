from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('courses', views.courses, name='courses'),
    path('trainers', views.trainers, name='trainers'),
    path('events', views.events, name='events'),
    path('course-detail', views.course_detail, name='course-detail')
]
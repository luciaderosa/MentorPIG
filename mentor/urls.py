from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index, name= 'index'),
    path("about/", views.about, name= 'about'),
    path("contact/", views.contact, name= 'contact'),
    path("courses/", views.courses, name= 'courses'),
    path("events/", views.events, name= 'events'),
    path("trainers/", views.trainers, name= 'trainers'),
    path("course-details/", views.course_details, name= 'course_details'),
]
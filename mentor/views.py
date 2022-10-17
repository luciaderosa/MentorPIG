from django.shortcuts import render
from mentordata.models import Event, Testimonial, Trainer, Course


# Create your views here.


def index(request):
    return render(request, 'mentor/index.html')


def contact(request):
    return render(request, 'mentor/contact.html')


def about(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'mentor/about.html', {'testimonials': testimonials})


def courses(request):
    courses = Course.objects.all()
    return render(request, 'mentor/courses.html', {'courses': courses})


def trainers(request):
    trainers = Trainer.objects.all()
    return render(request, 'mentor/trainers.html', {'trainers': trainers})


def events(request):
    events = Event.objects.all()
    return render(request, 'mentor/events.html', {'events': events})


def course_detail(request):
    return render(request, 'mentor/course-details.html')

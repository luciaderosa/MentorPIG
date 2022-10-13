from django.shortcuts import render
from mentordata.models import Event


# Create your views here.


def index(request):
    return render(request, 'mentor/index.html')


def contact(request):
    return render(request, 'mentor/contact.html')


def about(request):
    return render(request, 'mentor/about.html')


def courses(request):
    return render(request, 'mentor/courses.html')


def trainers(request):
    return render(request, 'mentor/trainers.html')


def events(request):
    events = Event.objects.all()
    return render(request, 'mentor/events.html', {'events': events})


def course_detail(request):
    return render(request, 'mentor/course-details.html')

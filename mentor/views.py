from django.shortcuts import render


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
    return render(request, 'mentor/events.html')     


def course_detail(request):
    return render(request, 'mentor/course-details.html')           
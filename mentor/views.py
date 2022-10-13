from django.shortcuts import render,HttpResponse
from mentordata.models import Event

# Create your views here.
def index(request):
    return render(request,'mentor/index.html')

def about(request):
    return render(request,'mentor/about.html')

def contact(request):
    return render(request,'mentor/contact.html')

def courses(request):
    return render(request,'mentor/courses.html')

def course_details(request):
    return render(request,'mentor/course-details.html')    

def events(request):
    events = Event.objects.all()
    return render(request, 'mentor/events.html', {'events': events})     
    
def trainers(request):
    return render(request,'mentor/trainers.html')            
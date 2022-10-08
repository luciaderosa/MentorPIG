from tabnanny import verbose
from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)                
    text = models.CharField(max_length=255)             
    img_path = models.CharField(max_length=100)   
    date = models.DateTimeField()

    def __str__(self):
        return self.title
    
    # events.html 
    # <div class="card">
    #     <div class="card-img">
    #         <img src="{% static 'mentor/img/events-1.jpg' %}" alt="..." /> (img_path)
    #     </div>
    #     <div class="card-body">
    #         <h5 class="card-title"><a href="">Introduction to webdesign</a></h5>(title)
    #         <p class="fst-italic text-center">
    #           Sunday, September 26th at 7:00 pm   (date)
    #         </p>
    #         <p class="card-text">
    #           Lorem ipsum dolor sit amet, consectetur elit, sed do eiusmod      (text)
    #           tempor ut labore et dolore magna aliqua. Ut enim ad minim veniam,
    #           quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
    #           commodo consequat
    #         </p>
    #     </div>
    # </div>
    # !!! deberíamos tener un campo con el detalle de la conferencia, pero para este ejemplo creo es mucho
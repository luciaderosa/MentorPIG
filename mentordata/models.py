from pickletools import ArgumentDescriptor
from django.db import models

# Create your models here.

#anterior a modificar
# class Event(models.Model):
#     title = models.CharField(max_length=100)                
#     text = models.CharField(max_length=255)             
#     img_path = models.CharField(max_length=100)   
#     date = models.DateTimeField()

#     def __str__(self):
#         return self.title

class Event(models.Model):
    # Campos y atributos
    # max_length= 20 — Establece que la longitud máxima del valor de este campo es 20 caracteres.
    # help_text="texto..." — proporciona una etiqueta de texto para mostrar que ayuda.

    title = models.CharField(max_length=100, help_text="Título del evento")                
    text =models.CharField(max_length=255,help_text="Resumen del evento")
    date=models.DateTimeField(help_text="Fecha y hora del evento")
    image = models.ImageField(upload_to ="projects")
    created=models.DateTimeField(auto_now_add = True)
    updated=models.DateTimeField(auto_now = True)  

    # Metadata
    class Meta:
    # para que el evento más nuevo quedo primero    
        ordering = ["-date"]

    # Métodos
   
    def __str__(self):
        #Cadena para representar el objeto MyModelName (en el sitio de Admin, etc.)
        return self.title
    
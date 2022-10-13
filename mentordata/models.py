from django.db import models

# Create your models here.


class Event(models.Model):
    # Campos y atributos
    # max_length= 20 — Establece que la longitud máxima del valor
    # de este campo es 20 caracteres.
    # help_text="texto..." — proporciona una etiqueta de texto
    # para mostrar que ayuda.

    title = models.CharField(max_length=100, help_text="Título del evento")
    # Cadena para representar el objeto MyModelName
    # (en el sitio de Admin, etc.)
    text = models.TextField(help_text="Resumen del evento")
    date = models.DateTimeField(help_text="Fecha y hora del evento")
    image = models.ImageField(upload_to="projects")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Metadata
    class Meta:
        # para que el evento más nuevo quedo primero
        ordering = ["-date"]

    # Métodos

    def __str__(self):
        # Cadena para representar el objeto MyModelName
        # (en el sitio de Admin, etc.)
        return self.title


class Trainer(models.Model):

    first_name = models.CharField(max_length=100, help_text="Nombre")
    last_name = models.CharField(max_length=100, help_text="Apellido")
    title = models.CharField(max_length=100, help_text="Título")
    brief = models.TextField(help_text="Resumen curricular")
    photo = models.ImageField(upload_to="projects", help_text="Foto")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta ():
        ordering = ['last_name', 'first_name']

    def __str__(self):
        # Cadena para representar el objeto MyModelName
        # (en el sitio de Admin, etc.)
        return self.last_name + ", " + self.first_name


class Testimonial(models.Model):

    name = models.CharField(max_length=100, help_text="Nombre")
    title = models.CharField(max_length=100, help_text="Título")
    text = models.TextField(help_text="Texto del testimonio")
    image = models.ImageField(upload_to="projects")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        # el orden de ingreso? la fecha de creación?
        # del más viejo al más nuevo?
        ordering = ["created"]

    def __str__(self):
        return self.name

from django.contrib import admin
from mentordata.models import Event, Trainer, Testimonial, Course, Category

# Register your models here.

admin.site.register(Event)
admin.site.register(Trainer)
admin.site.register(Testimonial)
admin.site.register(Course)
admin.site.register(Category)

from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Batch)
admin.site.register(Trainer)
admin.site.register(TrainerTask)
admin.site.register(StudentCourseData)

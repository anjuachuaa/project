from django.contrib import admin
from .models import *

# Register your models here.
   

class department_display(admin.ModelAdmin):
    list_display=['dep_name']
class batch_display(admin.ModelAdmin):
    list_display=['batch_name']
class student_display(admin.ModelAdmin):
    list_display=['student_name','Address','Dept']
admin.site.register(department,department_display)
admin.site.register(batch,batch_display)

admin.site.register(student,student_display)


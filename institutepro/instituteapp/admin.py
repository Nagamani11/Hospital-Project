from django.contrib import admin
from .models import CourseDetails

class CourseDetailsAdmin(admin.ModelAdmin):
    list_display =['course_no','course_name','course_fee','course_date','course_time','duration','trainer_name','experience']
admin.site.register(CourseDetails,CourseDetailsAdmin)

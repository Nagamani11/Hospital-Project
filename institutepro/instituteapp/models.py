from django.db import models
class ContactData(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.BigIntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=50)
class CourseDetails(models.Model):
    course_no = models.IntegerField()
    course_name = models.CharField(max_length=50)
    course_fee = models.BigIntegerField()
    course_date = models.DateField()
    course_time = models.TimeField()
    duration = models.CharField(max_length=50)
    trainer_name = models.CharField(max_length=50)
    experience = models.CharField(max_length=50)

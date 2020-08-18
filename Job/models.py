from django.db import models

# Create your models here.
class Job(models.Model): #table
    Full_Time = "Full Time"
    Part_Time = "Part Time"

    job_type_CHOICES = [
        (Full_Time,"Full Time"),
        (Part_Time,"Part Time")
    ]

    title = models.CharField(max_length = 100) #Colume
    # location
    job_type = models.CharField(max_length = 15,choices = job_type_CHOICES)
    description = models.TextField(max_length = 1000)
    published_at = models.DateTimeField(auto_now_add = True)
    vacancy = models.IntegerField(default = 1)
    salary = models.FloatField(default = 0.0)
    # Category
    experience = models.IntegerField(default = 0)

    def __str__(self):
        return self.title
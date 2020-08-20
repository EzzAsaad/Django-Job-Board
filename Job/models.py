from django.db import models
from django.utils.text import slugify


def upload_image(instance, filename):
    photoName, extension = filename.split('.')
    return "jobs/%s.%s" % (instance.id, extension)


# Create your models here.
class Job(models.Model):  #table
    Full_Time = "Full Time"
    Part_Time = "Part Time"

    job_type_CHOICES = [(Full_Time, "Full Time"), (Part_Time, "Part Time")]

    title = models.CharField(max_length=100)  #Colume
    # location
    job_type = models.CharField(max_length=15, choices=job_type_CHOICES)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now_add=True)
    vacancy = models.IntegerField(default=1)
    salary = models.FloatField(default=0.0)
    # Category
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    experience = models.IntegerField(default=0)
    image = models.ImageField(upload_to=upload_image)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
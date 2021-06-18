from django.db import models

# creating a class using the model manager. Detailing the kind of attributes each instance of this class will have when created.
class djangoClasses(models.Model):
    Title = models.CharField(max_length=50, default="", blank=True, null=False)
    Course_Number = models.IntegerField()
    Instructor_Name = models.CharField(max_length=75, default="", blank=True, null=False)
    Duration = models.FloatField()

    objects = models.Manager()

    def __str__(self):
        return self.Title
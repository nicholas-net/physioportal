from django.conf import settings
from django.db import models


# Patient inherits the functionalities to interact with the database
class Patient(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    medical_history = models.CharField(max_length=255)

    # Establish one to one relationship with user model
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)


class Exercises(models.Model):
    exercise_name = models.CharField(max_length=255)





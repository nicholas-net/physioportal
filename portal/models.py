from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import CASCADE
from django.utils.translation import gettext_lazy as _


class Exercise(models.Model):
    #Enums for consistent choices
    class BodyPart(models.TextChoices):
        HAND = "HA", _("Wrist")
        LEG = "LE", _("Leg")
        NECK = "NE", _("Neck")
        BACK = "BA", _("Back")
        FOOT = "FO", _("Foot")
        SHOULDER = "SH", _("Shoulder")
        ARM = "AR", _("Arm")
        CORE = "CO", _("Core")

    name = models.CharField(max_length=255)
    body_part = models.CharField(max_length=2, choices=BodyPart, default=BodyPart.CORE)
    type = models.CharField(max_length=255)
    instructions = models.TextField()
    equipment = models.CharField(max_length=255)

# Patient inherits the functionalities to interact with the database
class Patient(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    medical_history = models.CharField(max_length=255)

    # Establish one-to-one relationship with user model
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    # Program hasn't been defined yet so program is referenced lazily
    programs = models.ManyToManyField(Exercise, through="Program")

# negative set and rep counts doesn't make any sense
def validate_min(value):
    if value < 0:
        raise ValidationError(f"{value} is not valid")

class Program(models.Model):
    """
    Deleting a patient or exercise will result in related records
    linked to that model being deleted
    """
    patient = models.ForeignKey(Patient, on_delete=CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=CASCADE)
    sets = models.IntegerField(validators=[validate_min])
    reps = models.IntegerField(validators=[validate_min])
    duration = models.IntegerField(validators=[validate_min])
    position = models.CharField(max_length=255)



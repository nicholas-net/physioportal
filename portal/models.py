from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import CASCADE
from django.utils.translation import gettext_lazy as _


class Exercise(models.Model):
    # Provides pre-defined consistent choices for parts of the body exercises will be targeting
    class BodyPart(models.TextChoices):
        HAND = "HA", _("Wrist")
        LEG = "LE", _("Leg")
        NECK = "NE", _("Neck")
        BACK = "BA", _("Back")
        FOOT = "FO", _("Foot")
        SHOULDER = "SH", _("Shoulder")
        ARM = "AR", _("Arm")
        GLUTE = "GL", _("Glute")
        CORE = "CO", _("Core")
        HIP = "HI", _("Hip")

    class Category(models.TextChoices):
        # All the categories the clinic uses for each exercise
        STRETCH = "ST", _("Stretch")
        STRENGTH = "SN", _("Strength")
        CONDITION = "CO", _("Condition")
        BALANCE = "BA", _("Balance")
        OTHER = "OT", _("Other")

    class Equipment(models.TextChoices):
        # Commonly used exercise equipment at the clinic
        DUMBBELLS = "DB", _("Dumbbells")
        PHYSIOBALL = "PB", _("Physioball")
        STRAP = "ST", _("Strap")
        THERABAND = "TB", _("Theraband")
        BIKE = "BK", _("Bike")
        TREADMILL = "TM", _("Treadmill")
        ANKLEWEIGHT = "AW", _("Ankle Weight")
        OTHER = "OT", _("Other")
        NONE = "NO", _("None")

    name = models.CharField(max_length=255)
    body_part = models.CharField(max_length=2, choices=BodyPart, default=BodyPart.CORE)
    category = models.CharField(max_length=255, choices=Category, default=Category.OTHER)
    equipment = models.CharField(max_length=2, choices=Equipment, default=Equipment.NONE)
    instructions = models.TextField(blank=True, default="")

# Patient inherits the functionalities to interact with the database
class Patient(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    medical_history = models.CharField(max_length=255)

    # Establish one-to-one relationship with user model
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    # Program hasn't been defined yet so program is referenced lazily
    # This means that a Patient can have many Exercises, linked through the Program Table
    programs = models.ManyToManyField(Exercise, through="Program", related_name="patients")

# negative set and rep counts doesn't make any sense
def validate_min(value):
    if value < 0:
        raise ValidationError(f"{value} is not valid")

class Program(models.Model):
    """
    Deleting a patient or exercise will result in related records linked to that model being deleted
    """

    class Position(models.TextChoices):
        SUPINE = "SU", _("Supine")
        PRONE = "PR", _("Prone")
        LATERAL = "LA", _("Lateral")
        STANDING = "ST", _("Standing")
        SITTING = "SI", _("Sitting")
        # There's non-common use position types that are rarely used, so other should suffice for those rare use cases
        OTHER = "OT", _("Other")

    patient = models.ForeignKey(Patient, on_delete=CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=CASCADE)
    sets = models.IntegerField(validators=[validate_min])
    reps = models.IntegerField(validators=[validate_min])
    duration = models.IntegerField(validators=[validate_min], null=True, default=None)
    position = models.CharField(max_length=2, choices=Position, default=Position.OTHER)



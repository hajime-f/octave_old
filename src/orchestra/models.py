from octave import settings
from django.db import models

class Orchestra(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL)

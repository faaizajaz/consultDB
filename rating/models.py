from django.db import models
from consultant.models import Consultant
from django.contrib.auth.models import User


class Rating(models.Model):
    """
    Description: Rating object created for consultants by OPM users
    """

    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    consultant = models.ForeignKey(Consultant, on_delete=models.CASCADE)

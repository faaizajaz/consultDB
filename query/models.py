from django.db import models
from django.contrib.auth.models import User
from expertise.models import PracticeArea, Specialization, Skill

class ConsultantQuery(models.Model):
    """
    Description: Query for a consultant
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    practice_areas = models.ManyToManyField(PracticeArea)
    specializations = models.ManyToManyField(Specialization)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return f'Query by {self.user}'


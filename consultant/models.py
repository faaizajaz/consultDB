from django.db import models
from expertise.models import PracticeArea, Specialization, Skill


class Consultant(models.Model):
    """
    Description: The consultant object
    """

    #####################
    # Consultant populated fields
    #####################

    first_name = models.CharField(verbose_name="First name", max_length=500)
    last_name = models.CharField(verbose_name="Last name", max_length=500)
    experience_years = models.IntegerField(verbose_name="Years of experience")

    # Area of expertise - one to many linkages to expertise models
    practice_areas = models.ManyToManyField(PracticeArea, blank=True)
    specializations = models.ManyToManyField(Specialization, blank=True)
    skills = models.ManyToManyField(Skill, blank=True)


    # CV - one to one relation to file uploaded

    #####################
    # Computed fields
    #####################

    date_created = models.DateField(verbose_name="Date consultant was added", auto_now=True)
    date_updated = models.DateField(verbose_name="Date of last update", auto_now=True)
    

    #####################
    # Internally populated fields
    #####################
    
    # Rating - one to many link with ratings model

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse



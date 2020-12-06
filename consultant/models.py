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
    practice_areas = models.ManyToManyField(PracticeArea)
    specializations = models.ManyToManyField(Specialization)
    skills = models.ManyToManyField(Skill)


    # CV - one to one relation to file uploaded

    #####################
    # Computed fields
    #####################

    date_created = models.DateField(verbose_name="Date consultant was added")
    date_updated = models.DateField(verbose_name="Date of last update")
    

    #####################
    # Internally populated fields
    #####################
    
    # Rating - one to many link with ratings model


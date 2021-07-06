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
    practice_areas = models.ManyToManyField(PracticeArea)
    specializations = models.ManyToManyField(Specialization, blank=True)
    skills = models.ManyToManyField(Skill, blank=True)
    cv_file_1 = models.FileField(blank=True, null=True, verbose_name="CV slot 1")
    cv_file_2 = models.FileField(blank=True, null=True, verbose_name="CV slot 2")
    cv_file_3 = models.FileField(blank=True, null=True, verbose_name="CV slot 3")
    day_rate = models.IntegerField(verbose_name="Daily rate in PKR")
    email = models.EmailField(
        verbose_name="Consultant's email address", blank=True, null=True, unique=True
    )

    #####################
    # Computed fields
    #####################

    date_created = models.DateField(
        verbose_name="Date consultant was added", auto_now=True
    )
    date_updated = models.DateField(verbose_name="Date of last update", auto_now=True)
    form_complete = models.BooleanField(default=False)
    previous_engagement = models.BooleanField(default=False)
    query_score = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse('consultant-view', args=[str(self.id)])

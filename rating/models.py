from django.db import models
from consultant.models import Consultant


class Rating(models.Model):
    """
    Description: Rating object created for consultants by OPM users
    """

    creator = models.CharField(verbose_name="Your name", max_length=500)
    consultant = models.ForeignKey(Consultant, on_delete=models.CASCADE)
    project_code = models.CharField(
        verbose_name="OPM project code", max_length=10, null=True, blank=True
    )
    star_rating = models.IntegerField(verbose_name="Rating from 1-5", default=0)
    comment = models.TextField(verbose_name="Additional comments")
    date_of_engagement = models.CharField(
        verbose_name="Year of engagement", null=True, blank=True, max_length=200
    )
    days_worked = models.IntegerField(
        verbose_name="Number of days contracted", null=True, blank=True
    )
    contracted_rate = models.IntegerField(
        verbose_name="Rate at which consultant was contracted", null=True, blank=True
    )

    def __str__(self):
        return f'Rating for {self.consultant} by {self.creator}'

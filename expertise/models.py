from django.db import models


class PracticeArea(models.Model):
    """
    Description: The broad practice area/s of expertise. Align with portfolios.
    """

    name = models.CharField(verbose_name="Practice area name", max_length=500)

    def __str__(self):
        return f'{self.name}'


class Specialization(models.Model):
    """
    Description: Specialization within a practice area
    """

    name = models.CharField(verbose_name="Specialization name", max_length=500)
    practice_area = models.ForeignKey(PracticeArea, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} in {self.practice_area}'


class Skill(models.Model):
    """
    Description: Skills unrelated to practice areas (e.g. software, techniques)
    """

    name = models.CharField(verbose_name="Skill name", max_length=500)

    def __str__(self):
        return f'{self.name}'

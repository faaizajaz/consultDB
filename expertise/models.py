from django.db import models


class PracticeAreaManager(models.Manager):

    def get_by_natural_key(self, name):
        return self.get(name=name)

class PracticeArea(models.Model):
    """
    Description: The broad practice area/s of expertise. Align with portfolios.
    """

    name = models.CharField(verbose_name="Practice area name", max_length=500)

    objects = PracticeAreaManager()

    def __str__(self):
        return f'{self.name}'

    def natural_key(self):
        return(self.name)

class SpecializationManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)

class Specialization(models.Model):
    """
    Description: Specialization within a practice area
    """

    name = models.CharField(verbose_name="Specialization name", max_length=500)
    practice_area = models.ForeignKey(PracticeArea, on_delete=models.CASCADE)

    objects = SpecializationManager()

    def __str__(self):
        return f'{self.name}'

    def natural_key(self):
        return(self.name)

class SkillManager(models.Manager):

    def get_by_natural_key(self, name):
        return self.get(name=name)

class Skill(models.Model):
    """
    Description: Skills unrelated to practice areas (e.g. software, techniques)
    """

    name = models.CharField(verbose_name="Skill name", max_length=500)

    objects = SkillManager()

    def __str__(self):
        return f'{self.name}'

    def natural_key(self):
        return(self.name)

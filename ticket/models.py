from django.db import models

class Ticket(models.Model):

    opened_by = models.CharField(verbose_name="Your name", max_length=500)
    description = models.TextField(verbose_name="Description of the issue", max_length=500)

    def __str__(self):
        return f'Ticket opened by {self.opened_by}'


from django import forms
from .models import Ticket

class AddTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['opened_by', 'description']
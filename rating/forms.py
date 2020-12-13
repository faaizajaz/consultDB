from django import forms
from consultant.models import Consultant


class RatingSearchForm(forms.ModelForm):
    """
    Description:    The form used to search for consultants to rate
    """

    # TODO: Single field search: replace with a single text field 
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta:
        model = Consultant
        fields = ['first_name', 'last_name']
from django import forms
from consultant.models import Consultant
from .models import Rating


class RatingSearchForm(forms.ModelForm):
    """
    Description:    The form used to search for consultants to rate
    """

    # I am too lazy to change this from a CBF, so just using the 'first_name' field
    # but actually the form data is used to query both first and last name in the 
    # RatingSearchView
    first_name = forms.CharField(required=True, label='Enter first and/or last name')


    class Meta:
        model = Consultant
        fields = ['first_name']

class RateConsultantForm(forms.ModelForm):
    """
    Description:    The form used to rate a consultant
    """

    class Meta:
        model = Rating
        exclude = ['consultant']
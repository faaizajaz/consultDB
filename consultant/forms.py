from django import forms
from .models import Consultant
from expertise.models import PracticeArea, Specialization, Skill


class BioForm(forms.ModelForm):
    """
    Description: The first of three consultant creation forms. This creates the
                 consultant and populates the initial data.
    """
    first_name = forms.CharField(required=True, max_length=500)
    last_name = forms.CharField(required=True, max_length=500)
    experience_years = forms.IntegerField(required=True)

    class Meta:

        model = Consultant
        fields = ['first_name', 'last_name', 'experience_years']

class PracticeAreaForm(forms.ModelForm):
    """
    Description:    The second consultant creation form. This populates
                    the practice area field.
    """
    practice_areas = forms.ModelMultipleChoiceField(queryset=PracticeArea.objects.all(), required=True)

    class Meta:
        model = Consultant
        fields = ['practice_areas']

class SpecializationForm(forms.ModelForm):
    """
    Description:    The third consultant creation form. This populates
                    the specialization field.
    """
    class Meta:
        model = Consultant
        fields = ['specializations']

    def __init__(self, consultant_practice_areas, *args, **kwargs):
        super(SpecializationForm, self).__init__(*args, **kwargs)
        self.fields['specializations'].queryset = Specialization.objects.filter(practice_area__in=consultant_practice_areas)
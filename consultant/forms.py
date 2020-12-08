from django import forms
from .models import Consultant
from expertise.models import PracticeArea, Specialization, Skill


class BioForm(forms.ModelForm):
    """
    Description:    The first of five consultant creation forms. This creates the
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
                    the specializations field. The fields for the rendered form are filtered
                    based on the practice areas chosen in the previous form
    """
    class Meta:
        model = Consultant
        fields = ['specializations']

    def __init__(self, consultant_practice_areas, *args, **kwargs):
        super(SpecializationForm, self).__init__(*args, **kwargs)
        self.fields['specializations'].queryset = Specialization.objects.filter(practice_area__in=consultant_practice_areas)

class SkillForm(forms.ModelForm):
    """
    Description:    The fourth consultant creation form. This populates the skills field.
    """
    class Meta:
        model = Consultant
        fields = ['skills']

class CVForm(forms.ModelForm):
    """
    Description:    The final consultant creation form. This allows the consultant to
                    upload a CV.
    """
    class Meta:
        model = Consultant
        fields = ['cv_file']



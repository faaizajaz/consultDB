from django import forms
from .models import Consultant
from expertise.models import PracticeArea, Specialization, Skill
from .fields import GroupedModelMultipleChoiceField


class BioForm(forms.ModelForm):
    """
    Description:    The first of five consultant creation forms. This creates the
                    consultant and populates the initial data.
    """
    first_name = forms.CharField(required=True, max_length=500)
    last_name = forms.CharField(required=True, max_length=500)
    experience_years = forms.IntegerField(required=True)
    day_rate = forms.IntegerField(required=True)

    class Meta:

        model = Consultant
        fields = ['first_name', 'last_name', 'experience_years', 'day_rate']

class PracticeAreaForm(forms.ModelForm):
    """
    Description:    The second consultant creation form. This populates
                    the practice area field.
    """
    practice_areas = forms.ModelMultipleChoiceField(
        queryset=PracticeArea.objects.all(),
        required=True,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Consultant
        fields = ['practice_areas']

class SpecializationForm(forms.ModelForm):
    """
    Description:    The third consultant creation form. This populates
                    the specializations field. The fields for the rendered form are filtered
                    based on the practice areas chosen in the previous form
    """
    specializations = GroupedModelMultipleChoiceField(
        # This queryset is replaced in the constructor override below
        queryset=Specialization.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        choices_groupby='practice_area'
    )

    class Meta:
        model = Consultant
        fields = ['specializations']

    # Override constructor to only show models related to the selected practice areas.practice
    #
    # Here I added an extra parameter ("consultant_practice_areas") that takes a queryset of
    # all the practice areas selected by a consultant, and filters for only the related
    # specialization objects.
    def __init__(self, consultant_practice_areas, *args, **kwargs):
        super(SpecializationForm, self).__init__(*args, **kwargs)
        self.fields['specializations'].queryset = Specialization.objects.filter(practice_area__in=consultant_practice_areas)

class SkillForm(forms.ModelForm):
    """
    Description:    The fourth consultant creation form. This populates the skills field.
    """
    skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        required=True,
        widget=forms.CheckboxSelectMultiple
    )

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



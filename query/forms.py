from django import forms
from .models import ConsultantQuery
from expertise.models import PracticeArea, Specialization, Skill


class ConsultantQueryForm(forms.ModelForm):
    """
    Description: The consultant search form
    """

    practice_areas = forms.ModelMultipleChoiceField(
        queryset=PracticeArea.objects.all(),
        required=False
    )
    specializations = forms.ModelMultipleChoiceField(
        queryset=Specialization.objects.all(),
        required=False
    )
    skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        required=False
    )

    class Meta:
        model = ConsultantQuery
        exclude = ['user']

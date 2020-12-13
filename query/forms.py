from django import forms
from .models import ConsultantQuery
from expertise.models import PracticeArea, Specialization, Skill
from consultant.fields import GroupedModelMultipleChoiceField


class ConsultantQueryForm(forms.ModelForm):
    """
    Description: The consultant search form
    """

    practice_areas = forms.ModelMultipleChoiceField(
        queryset=PracticeArea.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )
    skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = ConsultantQuery
        exclude = ['user', 'specializations']

class SpecializationQueryForm(forms.ModelForm):
    """
    Description:    The optional specializations search form. This builds
                    specializations into the search query.
    """
    specializations = GroupedModelMultipleChoiceField(
        queryset=Specialization.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices_groupby='practice_area'
    )

    class Meta:
        model = ConsultantQuery
        fields = ['specializations']

    def __init__(self, consultant_practice_areas, *args, **kwargs):
        super(SpecializationQueryForm, self).__init__(*args, **kwargs)
        self.fields['specializations'].queryset = Specialization.objects.filter(practice_area__in=consultant_practice_areas)
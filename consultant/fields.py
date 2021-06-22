from functools import partial
from itertools import groupby
from operator import attrgetter
from django.forms.models import ModelChoiceIterator, ModelMultipleChoiceField


class GroupedModelChoiceIterator(ModelChoiceIterator):
    """
    Description:    A custom ModelChoiceIterator to allow us to group choices
                    by some related field
    """
    def __init__(self, field, groupby):
        self.groupby = groupby
        super().__init__(field)

    def __iter__(self):
        if self.field.empty_label is not None:
            yield ("", self.field.empty_label)
        queryset = self.queryset

        if not queryset._prefetch_related_lookups:
            queryset = queryset.iterator()
        for group, objs in groupby(queryset, self.groupby):
            yield (group, [self.choice(obj) for obj in objs])


class GroupedModelMultipleChoiceField(ModelMultipleChoiceField):
    """
    Description:    A custom ModelMultipleChoiceField that uses the
                    GroupedModelChoiceIterator
    """
    def __init__(self, *args, choices_groupby, **kwargs):
        if isinstance(choices_groupby, str):
            choices_groupby = attrgetter(choices_groupby)
        elif not callable(choices_groupby):
            raise TypeError('choices_groupby must either be a str or a callable with single arg')
        self.iterator = partial(GroupedModelChoiceIterator, groupby=choices_groupby)
        super().__init__(*args, **kwargs)

    # So that the field labels don't include practice area (I want PA names
    # for admin panel so its easy to see where a specialization belongs without
    # clicking into it)
    def label_from_instance(self, obj):
        return obj.name

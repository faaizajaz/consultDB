from django import template

register = template.Library()


@register.filter(name='specialization_display')
def specialization_display(consultant, specialization_queryset):
    output = []
    for specialization in specialization_queryset:
        if specialization in consultant.specializations.all():
            output.append(specialization)
    return output

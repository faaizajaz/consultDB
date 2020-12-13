from django.shortcuts import render
from .forms import ConsultantQueryForm
from django.db.models import Q
from consultant.models import Consultant
from django.core import serializers


def ConsultantQueryView(request):

    if request.method == 'POST':
        form = ConsultantQueryForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            query = Q()

            if data.get('practice_areas'):
                for practice_area in data.get('practice_areas'):
                    query.add(Q(practice_areas=practice_area), Q.AND)

            if data.get('specializations'):
                for specialization in data.get('specializations'):
                    query.add(Q(specializations=specialization), Q.AND)

            if data.get('skills'):
                for skill in data.get('skills'):
                    query.add(Q(skills=skill), Q.AND)

            # TODO: Remove serialization since I probably won't use Vue
            # Serialize results for consumption by Vue in template
            results_to_serialize = Consultant.objects.filter(query)

            result = serializers.serialize(
                'json',
                results_to_serialize,
                use_natural_foreign_keys=True
            )

            return render(request, 'query/results.html', {'result': result})

    else:
        form = ConsultantQueryForm()

    return render(request, 'query/consultant_search.html', {'form': form})


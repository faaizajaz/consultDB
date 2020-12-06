from django.shortcuts import render
from .forms import ConsultantQueryForm
from django.db.models import Q
from consultant.models import Consultant

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
                    print(specialization)
                    query.add(Q(specializations=specialization), Q.AND)

            if data.get('skills'):
                for skill in data.get('skills'):
                    print(skill)
                    query.add(Q(skills=skill), Q.AND)

            result = Consultant.objects.filter(query)

            return render(request, 'query/results.html', {'result': result})

    else:
        form = ConsultantQueryForm()

    return render(request, 'query/consultant_search.html', {'form': form})


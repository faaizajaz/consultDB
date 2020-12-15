from django.shortcuts import render, redirect
from .forms import ConsultantQueryForm, SpecializationQueryForm
from django.db.models import Q
from consultant.models import Consultant
from .models import ConsultantQuery


def ConsultantQueryView(request):

    if request.method == 'POST':
        if 'search' in request.POST:
            form = ConsultantQueryForm(request.POST)

            if form.is_valid():
                data = form.cleaned_data
                query = Q()

                if data.get('practice_areas'):
                    for practice_area in data.get('practice_areas'):
                        query.add(Q(practice_areas=practice_area), Q.AND)

                if data.get('skills'):
                    for skill in data.get('skills'):
                        query.add(Q(skills=skill), Q.AND)

                result = Consultant.objects.filter(query)

                return render(request, 'query/results.html', {'result': result})
        if 'add-specializations' in request.POST:
            form = ConsultantQueryForm(request.POST)
            if form.is_valid():
                new_query = form.save(commit=False)
                new_query.user = request.user
                form.save()
                return redirect('specialization-query', query_id=new_query.id)

    else:
        form = ConsultantQueryForm()

    return render(request, 'query/consultant_search.html', {'form': form})


def SpecializationQueryView(request, **kwargs):
    new_query = ConsultantQuery.objects.get(id=kwargs['query_id'])
    query_practice_areas = new_query.practice_areas.all()
    if request.method == 'POST':
        form = SpecializationQueryForm(query_practice_areas, request.POST, instance=new_query)
        if form.is_valid():
            data = form.cleaned_data
            query = Q()
            # Don't really need to do this for practice areas if specializations are selected.
            #
            # if new_query.practice_areas:
            #     print(type(new_query.practice_areas.all())) # This is a queryset phew

            if data.get('specializations'):
                for specialization in data.get('specializations'):
                    query.add(Q(specializations=specialization), Q.AND)

            if new_query.skills:
                # Do the same here
                data['skills'] = new_query.skills.all()
                for skill in data.get('skills'):
                    query.add(Q(skills=skill), Q.AND)

            result = Consultant.objects.filter(query)
            return render(request, 'query/results.html', {'result': result})

    else:
        form = SpecializationQueryForm(query_practice_areas, instance=new_query)
    return render(request, 'query/specialization_search.html', {'form': form})

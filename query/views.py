from django.shortcuts import render, redirect
from .forms import ConsultantQueryForm, SpecializationQueryForm
from django.db.models import Q
from consultant.models import Consultant
from .models import ConsultantQuery
from django.contrib.auth.decorators import login_required

@login_required
def ConsultantQueryView(request):

    if request.method == 'POST':
        # if the search button is clicked, query only skills and PAs
        if 'search' in request.POST:
            form = ConsultantQueryForm(request.POST)

            if form.is_valid():
                data = form.cleaned_data
                query = Q()
                num_parameters = 0


                if data.get('practice_areas'):
                    for practice_area in data.get('practice_areas'):
                        query.add(Q(practice_areas=practice_area), Q.OR)
                        num_parameters += 1

                if data.get('skills'):
                    for skill in data.get('skills'):
                        query.add(Q(skills=skill), Q.OR)
                        num_parameters += 1

                result = Consultant.objects.filter(query).distinct()


                for consultant in result:
                    consultant.query_score = 0
                    temp_query_score = 0
                    for practice_area in data.get('practice_areas'):
                        if practice_area in consultant.practice_areas.all():
                            #consultant.query_score += 1
                            temp_query_score += 1
                    for skill in data.get('skills'):
                        if skill in consultant.skills.all():
                            temp_query_score += 1
                            #consultant.query_score += 1

                    if num_parameters != 0:
                        consultant.query_score = (temp_query_score / num_parameters) * 100
                    else:
                        consultant.query_score = 100

                    consultant.save()

                

                return render(request, 'query/results.html', {'result': result.order_by('-query_score')})

        # If the add specializations button is clicked, pass the current PA and skills data to 
        # specialization form
        if 'add-specializations' in request.POST:
            form = ConsultantQueryForm(request.POST)
            if form.is_valid():
                new_query = form.save(commit=False)
                # TODO: This throws an error if a user is not logged in
                new_query.user = request.user
                form.save()
                return redirect('specialization-query', query_id=new_query.id)

    else:
        form = ConsultantQueryForm()

    return render(request, 'query/consultant_search.html', {'form': form})

@login_required
def SpecializationQueryView(request, **kwargs):
    new_query = ConsultantQuery.objects.get(id=kwargs['query_id'])
    query_practice_areas = new_query.practice_areas.all()
    if request.method == 'POST':
        form = SpecializationQueryForm(query_practice_areas, request.POST, instance=new_query)
        if form.is_valid():
            data = form.cleaned_data
            query = Q()

            num_parameters = 0
            
            # Don't really need to do this for practice areas if specializations are selected.
            #
            # if new_query.practice_areas:
            #     print(type(new_query.practice_areas.all())) # This is a queryset phew

            if data.get('specializations'):
                for specialization in data.get('specializations'):
                    query.add(Q(specializations=specialization), Q.OR)
                    num_parameters += 1

            if new_query.skills:
                # Do the same here
                data['skills'] = new_query.skills.all()
                for skill in data.get('skills'):
                    query.add(Q(skills=skill), Q.OR)
                    num_parameters += 1

            result = Consultant.objects.filter(query).distinct()

            for consultant in result:
                consultant.query_score = 0
                temp_query_score = 0
                for specialization in data.get('specializations'):
                    if specialization in consultant.specializations.all():
                        temp_query_score += 1
                for skill in data.get('skills'):
                    if skill in consultant.skills.all():
                        temp_query_score += 1

                if num_parameters != 0:
                    consultant.query_score = (temp_query_score / num_parameters) * 100
                else:
                    consultant.query_score = 100

                consultant.save()


            return render(request, 'query/results.html', {'result': result.order_by('-query_score')})

    else:
        form = SpecializationQueryForm(query_practice_areas, instance=new_query)
    return render(request, 'query/specialization_search.html', {'form': form})

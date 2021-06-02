from django.shortcuts import render, redirect
from .forms import RatingSearchForm, RateConsultantForm
from consultant.models import Consultant
from django.contrib.auth.decorators import login_required

@login_required
def RatingSearchView(request):

    if request.method == 'POST':
        form = RatingSearchForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            # TODO: Single field search: use one search field to query both names
            first_name = data.get('first_name')
            last_name = data.get('last_name')

            result = Consultant.objects.filter(
                first_name__icontains=first_name,
                last_name__icontains=last_name
            )

            return render(request, 'rating/rating_search_results.html', {'result': result})
    else:
        form = RatingSearchForm()

    return render(request, 'rating/rating_consultant_search.html', {'form': form})

@login_required
def RateConsultantView(request, **kwargs):
    consultant = Consultant.objects.get(id=kwargs['consultant_id'])

    if request.method == 'POST':
        form = RateConsultantForm(request.POST)

        if form.is_valid():
            # data = form.cleaned_data

            new_rating = form.save(commit=False)

            new_rating.consultant = consultant
            
            print("Current is:" + " " + str(new_rating.consultant.previous_engagement))

            if new_rating.consultant.previous_engagement is False:
                new_rating.consultant.previous_engagement = True
                new_rating.consultant.save()

            print("Current is:" + " " + str(new_rating.consultant.previous_engagement))

            new_rating.save()

            return redirect('consultant-view', consultant_id=consultant.id)
    else:
        form = RateConsultantForm()

    return render(request, 'consultant/rate-consultant.html', {'form': form, 'consultant': consultant})


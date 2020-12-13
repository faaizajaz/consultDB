from django.shortcuts import render
from .forms import RatingSearchForm
from django.db.models import Q
from consultant.models import Consultant


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

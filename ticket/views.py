from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import AddTicketForm

@login_required
def AddTicketView(request):
    if request.method == 'POST':
        form = AddTicketForm(request.POST)

        if form.is_valid():
            new_ticket = form.save(commit=False)
            new_ticket.save()
            return render(request, 'ticket/ticket-success.html')
    else:
        form = AddTicketForm()

    return render(request, 'ticket/add-ticket.html', {'form': form})


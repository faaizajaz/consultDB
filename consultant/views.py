from django.shortcuts import render, redirect
from django.views import generic
from .models import Consultant
from django.shortcuts import get_object_or_404
from .forms import BioForm, PracticeAreaForm
from django import forms

class ConsultantView(generic.DetailView):
    template_name = 'consultant/consultant-view.html'
    model = Consultant

    def get_object(self):
        return get_object_or_404(Consultant, pk=self.kwargs['consultant_id'])

def BioFormView(request, **kwargs):

    if request.method =='POST':
        form = BioForm(request.POST)
        if form.is_valid():
            new_consultant = form.save()
            print(new_consultant.id)
            return redirect('practice-area-view', consultant_id=new_consultant.id)
    else:
        form = BioForm()
    return render(request, 'consultant/add-consultant.html', {'form': form})

def PracticeAreaFormView(request, **kwargs):
    consultant = Consultant.objects.get(id=kwargs['consultant_id'])
    if request.method == 'POST':

        form = PracticeAreaForm(request.POST, instance=consultant)
        if form.is_valid():
            form.save()
            print(consultant.practicearea_set.all())
            print(type(consultant.practice_areas))
            return redirect('specialization-view', consultant_id=consultant.id)
    else:
        form = PracticeAreaForm(instance=consultant)
    return render(request, 'consultant/add-consultant.html', {'form': form})

def SpecializationFormView(request, **kwargs):
    consultant = Consultant.objects.get(id=kwargs['consultant_id'])



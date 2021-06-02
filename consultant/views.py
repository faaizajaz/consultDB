from django.shortcuts import render, redirect
from django.views import generic
from .models import Consultant
from django.shortcuts import get_object_or_404
from .forms import BioForm, PracticeAreaForm, SpecializationForm, SkillForm, CVForm
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin


class ConsultantView(LoginRequiredMixin, generic.DetailView):
    template_name = 'consultant/consultant-view.html'
    model = Consultant

    def get_object(self):
        return get_object_or_404(Consultant, pk=self.kwargs['consultant_id'])


def BioFormView(request, **kwargs):

    if request.method == 'POST':
        form = BioForm(request.POST)
        if form.is_valid():
            new_consultant = form.save()
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
            return redirect('specialization-view', consultant_id=consultant.id)
    else:
        form = PracticeAreaForm(instance=consultant)
    return render(request, 'consultant/add-consultant-practice-area.html', {'form': form, 'consultant': consultant})

def SpecializationFormView(request, **kwargs):
    consultant = Consultant.objects.get(id=kwargs['consultant_id'])
    consultant_practice_areas = consultant.practice_areas.all()
    if request.method == 'POST':
        form = SpecializationForm(consultant_practice_areas, request.POST, instance=consultant)
        if form.is_valid():
            form.save()
            return redirect('skill-view', consultant_id=consultant.id)
    else:
        form = SpecializationForm(consultant_practice_areas, instance=consultant)
    return render(request, 'consultant/add-consultant-specialization.html', {'form': form, 'consultant': consultant})

def SkillFormView(request, **kwargs):
    consultant = Consultant.objects.get(id=kwargs['consultant_id'])
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=consultant)
        if form.is_valid():
            form.save()
            return redirect('cv-view', consultant_id=consultant.id)
    else:
        form = SkillForm(instance=consultant)
    return render(request, 'consultant/add-consultant-skill.html', {'form': form, 'consultant': consultant})

def CVFormView(request, **kwargs):
    consultant = Consultant.objects.get(id=kwargs['consultant_id'])
    if request.method == 'POST':
        form = CVForm(request.POST, request.FILES, instance=consultant)
        if form.is_valid():
            # Set flag to indicate that consultant completed the form
            consultant.form_complete = True
            form.save()
            return redirect('consultant-view', consultant_id=consultant.id)
    else:
        form = CVForm(instance=consultant)
    return render(request, 'consultant/add-consultant-cv.html', {'form': form, 'consultant': consultant})




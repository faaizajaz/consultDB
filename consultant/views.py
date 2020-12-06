from django.shortcuts import render
from django.views import generic
from .models import Consultant
from django.shortcuts import get_object_or_404

class ConsultantView(generic.DetailView):
    template_name = 'consultant/consultant-view.html'
    model = Consultant

    def get_object(self):
        return get_object_or_404(Consultant, pk=self.kwargs['consultant_id'])

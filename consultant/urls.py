from django.urls import path
from . import views

urlpatterns = [
    path('add_consultant/', views.BioFormView, name='bioform'),
    path('<consultant_id>/', views.ConsultantView.as_view(), name='consultant-view'),
    path('<consultant_id>/pa/', views.PracticeAreaFormView, name='practice-area-view'),
    path('<consultant_id>/sp/', views.SpecializationFormView, name='specializaion-view')  
]
from django.urls import path
from . import views
import rating.views as RatingViews

urlpatterns = [
    path('add_consultant/', views.BioFormView, name='bioform'),
    path('<consultant_id>/', views.ConsultantView.as_view(), name='consultant-view'),
    path('<consultant_id>/pa/', views.PracticeAreaFormView, name='practice-area-view'),
    path('<consultant_id>/sp/', views.SpecializationFormView, name='specialization-view'),
    path('<consultant_id>/sk/', views.SkillFormView, name='skill-view'),
    path('<consultant_id>/cv/', views.CVFormView, name='cv-view'),
    path('<consultant_id>/rate/', RatingViews.RateConsultantView, name='rate-consultant-view')
]
from django.urls import path
from . import views

urlpatterns = [
    path('<consultant_id>', views.ConsultantView.as_view(), name='consultant-view')
]
from django.urls import path

from core import views
from django.views.generic import TemplateView

app_name = 'core'

urlpatterns = [
	path('pantry-detail/', views.pantry_detail, name='pantry-detail'),
    #
    #
]


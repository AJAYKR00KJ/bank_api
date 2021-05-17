from django.urls import path
from .views import autocomplete_branch

urlpatterns = [
    path('autocomplete/', autocomplete_branch),
]
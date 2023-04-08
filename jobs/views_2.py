"""
Django generic views
Applicant (Resource)
GET HTTP request
- singular
- plural
"""


from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from jobs.models import Applicant, Portal

from django.urls import reverse_lazy


class ApplicantList(ListView):
    """
    jobs/applicant_list.html
    """

    model = Applicant


class ApplicantCreate(CreateView):

    model = Applicant
    fields = ["name", "applied_for", "cover_letter"]
    success_url = reverse_lazy("v2-applicant-list")


class ApplicantUpdate(UpdateView):
    model = Applicant
    fields = ["id", "name", "cover_letter"]
    success_url = reverse_lazy("v2-applicant-list")


class ApplicantDelete(DeleteView):
    model = Applicant
    success_url = reverse_lazy("v2-applicant-list")
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import JsonResponse
from jobs.models import Portal, JobDescription


# Create your views here.
def welcome(request):

    cricketers = ["virat", "dhoni", "rahul", "sachin"]

    return render(
        request,
        "jobs/welcome.html",
        {"message": "Good morning", "cricketers": cricketers}
    )


def get_portal_details(request):
    """
    """
    ###############################################
    # how to get URL associated with django view? #
    ###############################################
    from django.urls import reverse
    print(reverse("portal_details"))

    objs = Portal.objects.order_by("id")

    portals = []
    for obj in objs:
        portals.append(obj.name)

    return JsonResponse(portals, safe=False)


def get_job_description(request, job_id):
    jd = get_object_or_404(JobDescription, pk=job_id)
    return render(request, "jobs/job_description.html", {"job_desc": jd})


# TODO 1 - write an API endpoint to get list of applicants (.../jobs/applicants)
# TODO 2 - write an API endpoint to get details of
#          single applicant (.../jobs/applicants/1)
# TODO 3 - write an API endpoint to get list of applicants (.../jobs/jobtitles)
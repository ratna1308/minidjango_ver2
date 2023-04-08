import json
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import JsonResponse
from jobs.models import Portal, JobDescription, JobTitle
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views import View
import pdb

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


@csrf_exempt
def job_titles(request):
    """plural endpoint to get all job titles"""

    if request.method == "POST":
        data = json.loads(request.body)
        # TODO - add validation for the request data.

        portal_data = data.get("portal")
        portal_name = portal_data.get("name")
        portal = Portal.objects.filter(name=portal_name)

        if not portal:
            portal = Portal.objects.create(**portal_data)
            portal.save()
        else:
            portal = portal[0]

        jd = data.get("job_description")
        jd_role = jd.get("role")
        jd_obj = JobDescription.objects.filter(role=jd_role)

        if not jd_obj:
            jd = JobDescription.objects.create(**jd)
            jd.save()
        else:
            jd = jd_obj[0]

        data["job_description"] = jd
        data["portal"] = portal
        jt = JobTitle.objects.create(**data)
        jt.save()

        job_titles = JobTitle.objects.all()
        return render(
            request,
            "jobs/job_titles.html",
            {"objects": job_titles}
        )


# TODO - write PATCH request for `job_title` resource
# TODO - write DELETE request for job_title` resource

# Create your function based view like following -
def welcome(request):

    cricketers = ["virat", "dhoni", "rahul", "sachin"]

    return render(
        request,
        "jobs/welcome.html",
        {"message": "Good morning", "cricketers": cricketers}
    )


# Create your class based view like following -
class WelcomeView(View):
    def get(self, request):
        # <view logic>
        return HttpResponse('welcome to first class based view')

    # @csrf_exempt
    def post(self, request):

        breakpoint()

        # write your post view logic here
        return HttpResponse("welcome to POST request using class based view")

    def patch(self, request):
        # write your PATCH request logic here
        return HttpResponse("welcome to PATCH request using class based view")

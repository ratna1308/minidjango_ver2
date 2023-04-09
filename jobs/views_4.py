from jobs.models import JobTitle, Portal
from jobs.serializers import JobTitleSerializer, PortalSerializer
from django.http import JsonResponse, HttpResponse


def jobtitle_list(request):

    if request.method == "GET":
        job_titles = JobTitle.objects.all()

        #############################################################
        # how to serialize multiple objects using DRF serializer?   #
        #############################################################
        job_titles = JobTitleSerializer(job_titles, many=True)

        # whenever data is in non-dict format we have to set `safe=False`
        return JsonResponse(job_titles.data, safe=False)

    elif request.method == "POST":
        pass


# TODO portals list
def portal_list(request):
    if request.method == "GET":
        portals = Portal.objects.all()
        portals_data = PortalSerializer(portals, many=True)

        ###################################################################
        # how validate serialized object against validation constraints?  #
        ###################################################################

        # SCENARIO 1 :: when you have multiple objects
        obj = PortalSerializer(data=portals_data.data, many=True)
        print(obj.is_valid())

        # To check errors (if any)
        print(obj.errors)

        # SCENARIO 2 :: when you have single object
        portal = portals[0]
        data = {"name": portal.name, "description": portal.description}
        obj = PortalSerializer(data=data)
        print(obj.is_valid())

        # To check errors (if any)
        print(obj.errors)


        return JsonResponse(portals_data.data, safe=False)
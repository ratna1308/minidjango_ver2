import json
from rest_framework.views import APIView
from rest_framework.response import Response
from jobs.models import Applicant
from django.contrib.auth.models import User


from rest_framework import serializers


class ApplicantSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=250)
    cover_letter = serializers.CharField(
        max_length=250,
        required=False,
        help_text="cover letter is brief description of your interests in particular job role")


class Applicants(APIView):
    def get(self, request):
        applicants = Applicant.objects.all()
        applicants = {"name": applicant.name for applicant in applicants}

        breakpoint()
        return Response(applicants)

    def post(self, request):
        data = json.loads(request.body)
        Applicant.objects.create(**kwargs)
        resp = {"message": "success", "records": ""}
        return Response(resp)

    def delete(self, request):
        data = json.loads(request.body)
        # TODO - write ORM query to delete record from database.
        pass


###############################################
# django default authentication system        #
###############################################

class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        final = dict()
        for user in users:
            final[user.id] = {"first_name": user.first_name,
                              "email": user.email}
        return Response(final)

from django.urls import path
from . import views
from . import views_2
from . import views_3
from . import views_4

"""
<home-url>/jobs/welcome/
<home-url>/jobs/portals/
# TODO
https://docs.djangoproject.com/en/4.1/topics/http/urls/#path-converters
"""


urlpatterns = [

    path('welcome/', views.welcome),
    # keyword argument `name` is passed to path function
    # these are called as named URLs
    path("portals/", views.get_portal_details, name="portal_details"),
    path("jobtitles/", views.job_titles, name="jobtitle"),
    path("jobtitles/<int:job_id>/", views.get_job_description, name="jd"),
    path("welcomeview/", views.WelcomeView.as_view(), name="welcomeview"),

    # class-based views using django generic views.
    path("v2/applicants/", views_2.ApplicantList.as_view(), name="v2-applicant-list"),
    path("v2/applicants/detail/<int:pk>", views_2.ApplicantDelete.as_view(), name="v2-applicant-detail-view"),
    path("v2/applicants/create/", views_2.ApplicantCreate.as_view(), name="v2-applicant-create"),
    path("v2/applicants/update/<int:pk>", views_2.ApplicantUpdate.as_view(), name="v2-applicant-update"),
    path("v2/applicants/delete/<int:pk>", views_2.ApplicantDelete.as_view(), name="v2-applicant-delete"),

    # V3 URLs (created for django-rest-framework using APIView)
    path(
        "v3/applicants/",
        views_3.Applicants.as_view(),
        name="v3_applicants_list"
    ),
    path(
        "v3/applicants/<int:pk>",
        views_3.Applicants.as_view(),
        name="v3_applicants_list"
    ),
    path("v3/users/",
         views_3.UserList.as_view(),
         name="v3_users_list"),


    # V4 URLs (created for job titles using DRF and serializers)
    path(
        "v4/jobtitles",
        views_4.jobtitle_list,
        name="v4_jobtitles_list"
    ),
    path(
        "v4/portals",
        views_4.portal_list,
        name="v4_portals_list"
    ),


]

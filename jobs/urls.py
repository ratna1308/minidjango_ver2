from django.urls import path
from . import views

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
    path("jobtitles/<int:job_id>/", views.get_job_description, name="jd")
]
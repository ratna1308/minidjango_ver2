1. django-admin startproject <project-name>
2. python manage.py runserver
3. Go to home-url, you will see default django welcome page
4. django-admin startapp app1
5. The only relative endpoint available at this stage is /admin
6. You cannot yet access admin page because admin is a application configured in settings.py
7. There are some pre-installed apps whenever we creat django project
8. For example django.contrib.admin is one of them
9. To access these projects we need to makemigrations & migrate first.
10. python manage.py makemigrations (detects changes related to application models)
11. python manage.py migrate (applies model changes to database)
12. Now you can access admin page, but you don't have application user yet.
13. python manage.py createsuperuser
14. I can log into admin interface using user created in above step.
15. You can now write new views in views.py file under application
16. We do URL binding of this view by adding URL mapping in urls.py file
17. We also need to register any new application that we create in settings.py
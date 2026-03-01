============
django-polls
============

django-polls is a Django app to conduct web-based polls.
For each question, visitors can choose between a
fixed number of answers.

Detailed documentation is in the "docs" directory

Quick start
-----------

1. Add "polls" to your INSTALLED_APP setting like this::
    INSTALLED_APPS = [
        ...,
        "django_polls",
    ]

2. include the polls URLconf in your project urls.py like thiss::
    path("polls/", include("django_polls.urls")),

3. Run ``python manage.py migrate`` to create the models.

4. Start the developement server and visit the admin to create a poll.

5. Visit the ``/polls/`` URL to participate in the poll.

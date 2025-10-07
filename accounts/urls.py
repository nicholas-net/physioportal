from django.urls import path
from .views import login_view

# Tells Django to look within our current directory for a view.py file

"""
path function anatomy:
    - the route itself
    - reference to the view function
"""
urlpatterns = [
    path("login/", login_view, name="login")
]
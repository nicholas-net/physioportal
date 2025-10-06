from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def login_view(request):
    """
    Users are routed to the log-in page for authentication

    Args:
        request: HttpRequest object

    Returns:
        HttResponse object for the portal log-in page
    """

    template = loader.get_template("login.html")
    return HttpResponse(template.render())
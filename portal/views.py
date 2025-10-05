from django.shortcuts import render
from django.http import HttpResponse


def home_page_view(request):
    """
    Handles requests for the home page resource.

    Args:
        request: HttpRequest object

    Returns:
        HttResponse object for the portal homepage
    """
    return HttpResponse("Portal Homepage")
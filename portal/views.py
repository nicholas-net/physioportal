from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def homepage_view(request):

    template = loader.get_template("portal/homepage.html")
    return HttpResponse(template.render())


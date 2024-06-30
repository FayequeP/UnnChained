import pathlib
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView


def home_page_view(request, *args, **kwargs):
    html_template = "base.html"
    return render(request, html_template)

def login(request):
    return LoginView.as_view(template_name='login.html')(request)
import pathlib
from pickle import FALSE, TRUE
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
from django.contrib.auth.views import LoginView
from django.urls import reverse, reverse_lazy

LOGIN_URL = settings.LOGIN_URL

def home_view(request, *args, **kwargs):
    html_template = "home.html"
    return render(request, html_template)

@login_required
def dashboard(request, *args, **kwargs):
    html_template = "dashboard/posts.html"
    return render(request, html_template)


@login_required
def system_prompts(request, *args, **kwargs):
    html_template = "dashboard/ai_setting/prompt.html"
    return render(request, html_template)

@login_required
def documents(request, *args, **kwargs):
    html_template = "dashboard/ai_setting/document.html"
    return render(request, html_template)

VALID_CODE = "1104"

@staff_member_required(login_url= LOGIN_URL)
def pw_protetected_view(request, *args, **kwargs):
    is_allowed = FALSE
    if request.method == "POST":
        user_pw_sent = request.POST.get("code") or None
        if user_pw_sent == VALID_CODE:
            is_allowed = TRUE
            return render(request, "account/signup.html", {})
        else:
            return HttpResponse("Invalid Code")
    return render(request, "protected/entry.html", {})

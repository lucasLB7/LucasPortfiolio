from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
import datetime as dt
import simplejson as json
from django.http import JsonResponse
import requests
from django.conf import settings


# from .models import LaminateFlooring

from django.http import HttpResponse, Http404, HttpResponseRedirect

from .models import Resume

# ////////////////////////////////////////////////////////////////////////////

def view_github_repos(request):
    user = requests.get('https://api.github.com/users/lucasLB7?access_token={}'.format(settings.GITHUB_API))
    user_content = json.loads(user.content)

    repos = requests.get('https://api.github.com/users/lucasLB7/repos?access_token={}'.format(settings.GITHUB_API))
    repo_content = json.loads(repos.content)


    return render(request, 'repositories/view-repos.html' , {"repos_details":repo_content , "user_details":user_content})

def homepage(request):
    return render(request, 'home/main.html')


def view_python(request):
    python_repos = Resume.objects.all()

    return render(request, 'python/main.html' , {"python":python_repos})
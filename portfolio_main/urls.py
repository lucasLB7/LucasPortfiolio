from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url


from . import views



app_name = "main"


urlpatterns = [
    url(r'^$', views.homepage, name = "homepage"),
    url(r'^repos$', views.view_github_repos, name = "repos"),
    url(r'my_python_apps$', views.view_python, name = "python")
]
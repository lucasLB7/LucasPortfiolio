from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url


from . import views



app_name = "main"


urlpatterns = [
    url(r'^$', views.homepage, name = "homepage"),
    url(r'^repos$', views.view_github_repos, name = "repos"),
    url(r'my_python_apps$', views.view_python, name = "python"),
    url(r'my_html_apps$', views.view_html, name = "html"),
    url(r'^my_blender_apps$', views.view_blender, name = "blender"),
    url(r'^view_all_categories$', views.view_all , name = "all_categories")
]
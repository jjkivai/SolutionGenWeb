from django.urls import path

from .views import *
from django.views.generic import TemplateView

app_name = 'SolutionsGenApp'

urlpatterns = [
    path("", view=TemplateView.as_view(template_name='index.html'), name="home"),
    path("services/", view=TemplateView.as_view(template_name='index.html'), name="services"),
    path("projects/", view=TemplateView.as_view(template_name='index.html'), name="projects"),
    path("about-us/", view=TemplateView.as_view(template_name='index.html'), name="about-us"),

]
from . import views
from django.views.generic import TemplateView
from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers

# URLConf
urlpatterns = [
    path("", TemplateView.as_view(template_name="core/index.html"))
]

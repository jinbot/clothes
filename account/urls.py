from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^login/$', views.index),
    url(r'^signup/$', views.signup),
]

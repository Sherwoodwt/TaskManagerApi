from django.conf.urls import url

from .views import tasks

urlpatterns = [
    url(r'^tasks/$', tasks),
]

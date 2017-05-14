from django.conf.urls import url

from .views import (
    tasks,
    task_by_id
)

urlpatterns = [
    url(r'^tasks/$', tasks),
    url(r'^tasks/(?P<task_id>[0-9]+)/$', task_by_id)
]

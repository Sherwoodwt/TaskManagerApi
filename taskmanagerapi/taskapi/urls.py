from django.conf.urls import url

from .views import (
    comments,
    comments_by_id,
    tasks,
    tasks_by_id
)

urlpatterns = [
    url(r'^tasks/$', tasks),
    url(r'^tasks/(?P<task_id>[0-9]+)/$', tasks_by_id),
    url(r'^comments/$', comments),
    url(r'^comments/(?P<comment_id>[0-9]+)/$', comments_by_id),
]

from django.conf.urls import url

from .views import (
    comments,
    comments_by_id,
    comments_by_task_id,
    tasks,
    tasks_by_id,
    users,
    users_by_id,
    tasks_by_assignee_id,
    tasks_by_created_by_id,
)

urlpatterns = [
    url(r'^tasks/$', tasks),
    url(r'^tasks/(?P<task_id>[0-9]+)/$', tasks_by_id),
    url(r'^comments/$', comments),
    url(r'^comments/(?P<comment_id>[0-9]+)/$', comments_by_id),
    url(r'^tasks/(?P<task_id>[0-9]+)/comments/$', comments_by_task_id),
    url(r'^users/$', users),
    url(r'^users/(?P<user_id>[0-9]+)/$', users_by_id),
    url(r'^users/(?P<user_id>[0-9]+)/assigned_tasks/$', tasks_by_assignee_id),
    url(r'^users/(?P<user_id>[0-9]+)/created_tasks/$', tasks_by_created_by_id),
]

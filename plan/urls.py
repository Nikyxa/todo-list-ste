from django.urls import path

from plan.views import TaskCreateView, TaskListView, TagListView, TaskUpdateView, TagCreateView, TagUpdateView, \
    TaskDeleteView, TagDeleteView, toggle_assign_to_tag

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path(
            "tags/<int:pk>/toggle-assign/",
            toggle_assign_to_tag,
            name="toggle-assign",
        ),
]

app_name = "plan"

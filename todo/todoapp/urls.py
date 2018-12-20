from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, ToDoDetailsView

urlpatterns = {
    url(r'^todolist/$', CreateView.as_view(), name="create"),
    url(r'^todolist/(?P<pk>[0-9]+)/$', ToDoDetailsView.as_view(), name="details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
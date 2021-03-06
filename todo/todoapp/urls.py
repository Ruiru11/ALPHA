from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, ToDoDetailsView, UserDetail, UserCreate
from .views import LoginView

urlpatterns = [
    url(r'^todolist/$', CreateView.as_view(), name="create"),
    url(r'^users/$', UserCreate.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
    url(r'^todolist/(?P<pk>[0-9]+)/$', ToDoDetailsView.as_view(), name="details"),
    url(r'^login/$', LoginView.as_view(), name='login',)
]

urlpatterns = format_suffix_patterns(urlpatterns)

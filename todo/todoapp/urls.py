from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, UserCreate

urlpatterns = [
    url(r'^todolist/$', CreateView.as_view(), name="create"),
    url("users/", UserCreate.as_view(), name="user_create"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
# urlpatterns = []
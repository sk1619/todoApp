from .views import TodoView
from django.conf.urls import url

urlpatterns = [
    url(r'^', TodoView.as_view())
]

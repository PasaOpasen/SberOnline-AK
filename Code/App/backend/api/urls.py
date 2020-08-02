from django.conf.urls import include, url
from rest_framework import routers

from api.http.views import ReviewCreateView

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^review', ReviewCreateView.as_view()),
]

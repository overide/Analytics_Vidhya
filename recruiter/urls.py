from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^search/$',search),
    url(r'^download_csv/$',create_csv_stream)
]

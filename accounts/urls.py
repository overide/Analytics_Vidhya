from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^register/$',register),
    url(r'^login/$',login_view),
    url(r'^logout/$',logout_view),
    # url(r'^ajax/$',ajax_handler),
]
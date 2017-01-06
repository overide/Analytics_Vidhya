from django.conf.urls import url
from .views import *
from .ajax_handler import *

urlpatterns = [
    url(r'^register/$',register),
    url(r'^login/$',login_view),
    url(r'^logout/$',logout_view),
    url(r'^ajax/validate_username/$',validate_username),
    url(r'^ajax/validate_email/$',validate_email),
]
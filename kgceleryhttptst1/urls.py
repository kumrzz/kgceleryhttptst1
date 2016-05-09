from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from testapp import views

urlpatterns = [
    url(r'^multiply/', views.multiply, name='multiply'),
]
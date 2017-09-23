# turns out this isn't made automatically

from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$', views.index, name='app1index'),
]
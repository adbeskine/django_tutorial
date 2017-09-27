# turns out this isn't made automatically

from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$', views.index, name='app1index'),
url(r'^indexgenvar/$', views.index_generated_variables, name='indexgenvar'),
url(r'^indexhtmllong/$', views.index_html_longhand, name='indexhtmllong'),
url(r'^indexhtmlshort/$', views.index_html_shorthand, name='indexhtmlshort'),
url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
url(r'^(?P<question_id>[0-9]+/results/$)', views.results, name='results'),
url(r'^(?P<question_id>[0-9]+/vote/$)', views.vote, name='vote')
]
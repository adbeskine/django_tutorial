# turns out this isn't made automatically

from django.conf.urls import url
from . import views

app_name = 'app1'

urlpatterns = [
url(r'^$', views.index, name='app1index'),
url(r'^indexgenvar/$', views.index_generated_variables, name='indexgenvar'),
url(r'^indexhtmllong/$', views.index_html_longhand, name='indexhtmllong'),
url(r'^indexhtmlshort/$', views.index_html_shorthand, name='indexhtmlshort'),
url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
url(r'^404enabled/(?P<question_id>[0-9]+)/$', views.detail_with_404, name='detailw404'),
url(r'^404shortcut/(?P<question_id>[0-9]+)/$', views.detail_404_shortcut, name='detail404shortcut'),
url(r'^(?P<question_id>[0-9]+/results/$)', views.results, name='results'),
url(r'^(?P<question_id>[0-9]+/vote/$)', views.vote, name='vote')
]
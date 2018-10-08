from django.conf.urls import url
from .views import (
	create_view,
	list_view,
	detail_view,
	update_view,
	delete_view
	)

urlpatterns = [
    url(r'^create', create_view, name='create'),
    url(r'^list', list_view, name='list'),
    url(r'^(?P<id>\d+)/$', detail_view, name='detail'),
    url(r'^(?P<id>\d+)/edit/$', update_view, name='update'),
    url(r'^(?P<id>\d+)/delete/$', delete_view, name='delete'),
]
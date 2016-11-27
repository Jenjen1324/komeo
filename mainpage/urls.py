from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^list$', views.list, name="list"),
	url(r'^p/(?P<project_id>[0-9A-Za-z-]+)/download$', views.project_download, name='project_download'),
	url(r'^p/(?P<project_id>[0-9A-Za-z-]+)/edit$', views.project_edit, name='project_edit'),
	url(r'^p/(?P<project_id>[0-9A-Za-z-]+)/$', views.project, name='project'),
	url(r'^login$', views.login_view, name='login'),
	url(r'^logout$', views.logout_view, name='logout'),
	url(r'^register$', views.register_view, name='register'),
	url(r'^activate/(?P<activation_key>[0-9A-Za-z-]+)/$', views.activate, name='activate'),
	url(r'^u/(?P<user_id>[0-9A-Za-z-]+)/$', views.profile, name='profile'),
	url(r'^create$', views.project_create, name='project_create'),
]

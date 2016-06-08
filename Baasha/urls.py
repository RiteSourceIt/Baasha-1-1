from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^language/$', views.language, name='language'),
    url(r'^$', views.index, name='index'),
]
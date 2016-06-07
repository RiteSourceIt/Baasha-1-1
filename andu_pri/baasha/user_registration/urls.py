from django.conf.urls import url
from django.contrib import admin
from user_registration.views import index,dashboard,signmeup,dologout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/',index,name="index"),
    url(r'^dashboard/',dashboard,name="dashboard"),
    url(r'^signmeup/',signmeup,name="signmeup"),
    url(r'^logout/',dologout,name="logout"),
]
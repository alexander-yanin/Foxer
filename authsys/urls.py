from django.conf.urls import url
from . import views

app_name = 'authsys'
urlpatterns = [
    url(r'^$', views.home_auth, name='home_auth'),
    url(r'^reg/$', views.reg, name='reg'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
]

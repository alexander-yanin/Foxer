from django.conf.urls import url
from . import views

app_name = 'cabinet'
urlpatterns = [
    url(r'^$', views.home_cabinet, name='home_cabinet'),
    url(r'^profil/$', views.profil, name='profil'),
    url(r'^profil/upload/$', views.upload, name='upload'),
    url(r'^profil/publication/$', views.publication, name='publication'),
    url(r'^profil/publication/delete/(?P<pk>\d*)/$',
        views.delete_publication, name='delete_publication'),
    url(r'^profil/sold/$', views.sale, name='sale'),
    url(r'^profil/purchases/$', views.purchase, name="purchase"),
]

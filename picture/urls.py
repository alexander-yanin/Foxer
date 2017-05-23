from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from . import views


app_name = 'picture'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<pk>\d*)/$', views.home_picture, name='home_picture'),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )

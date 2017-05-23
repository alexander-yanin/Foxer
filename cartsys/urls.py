from django.conf.urls import url
from . import views


app_name = 'cartsys'
urlpatterns = [
    url(r'^$', views.home_cart, name='home_cart'),
    # url(r'^add/$', views.add_in_cart, name='add_in_cart'),
    # url(r'^delete/$', views.delete_from_cart, name='delete_from_cart'),
    url(r'payment/$', views.payment, name='payment'),
]

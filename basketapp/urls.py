from django.urls import path
from django.conf.urls import url
from .views import basket, basket_add, basket_remove, add

app_name = 'basketapp'

urlpatterns = [
    url(r'^$', basket, name='basket_view'),
    url(r'^add_product/(?P<pk>\d+)/$', basket_add, name='add_product'),
    url(r'^add/(?P<pk>\d+)/$', add, name='add'),
    url(r'^remove/(?P<pk>\d+)/$', basket_remove, name='remove_product'),
]

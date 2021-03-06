from django.urls import path
from . import views
from django.conf.urls import url
from .views import index, product_list, product_detail, product_category

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^product_list/$', product_list, name='product_list'),
    url(r'^product_category/(?P<pk>\d+)/$', product_category, name='product_category'),
    url(r'^product_detail/(?P<pk>\d+)/$', product_detail, name='product_detail'),

    # ------------------------------

]

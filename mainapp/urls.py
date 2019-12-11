from django.urls import path
from . import views
from django.conf.urls import url
from .views import index, product_list, product_detail



urlpatterns = [
    url(r'^$', index, name='index'),
    path('product_list/', product_list, name = 'product_list'),
    url(r'^product_list/product_detail/(?P<pk>\d+)/$', product_detail, name ='product_detail'),
 
#------------------------------

]

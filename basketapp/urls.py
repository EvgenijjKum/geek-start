from django.urls import path
from django.conf.urls import url
from .views import basket, basket_add, basket_remove

app_name = 'basketapp'

urlpatterns = [
    url(r'^$', basket, name='basket_view'),
    path('add/<int:pk>/', basket_add, name='add'),
    path('remove/<int:pk>)/', basket_remove, name='remove'),
]

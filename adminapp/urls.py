from django.urls import path
from .views import *

app_name = 'adminapp'


urlpatterns = [
    # --- START CRUD for product ---
    path('list-product/', ProductListView.as_view(), name='list-all-product'),
    path('create-product/', ProductCreate.as_view(), name='create-product'),
    path('read-product-detail/<int:pk>/', ProductDetail.as_view(), name='view-product-detail'),
    path('update-product/<int:pk>/', ProductUpdate.as_view(), name='update-product'),
    path('delete-product/<int:pk>/', ProductDelete.as_view(), name='delete-product'),
    # --- END CRUD for product ---

    # --- START CRUD for category ---
    path('list-category/', CategoryListView.as_view(), name='list-category'),
    path('create-category/', CategoryCreate.as_view(), name='create-category'),
    path('read-category-detail/<int:pk>/', ProductCategoryDetail.as_view(), name='view-category-detail'),
    path('update-category/<int:pk>/', CategoryUpdate.as_view(), name='update-category'),
    path('delete-category/<int:pk>/', CategoryDelete.as_view(), name='delete-category'),
    # --- END CRUD for category ---

    # --- START CRUD for user ---
    path('list-user/', UserListView.as_view(), name='list-user'),
    path('create-user/', UserCreate.as_view(), name='create-user'),
    path('read-user-detail/<int:pk>/', UserDetail.as_view(), name='view-user-detail'),
    path('update-user/<int:pk>/', UserUpdate.as_view(), name='update-user'),
    path('delete-user/<int:pk>/', UserDelete.as_view(), name='delete-user'),
    # --- END CRUD for user ---

]

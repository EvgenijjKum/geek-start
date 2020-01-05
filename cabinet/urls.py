from django.urls import path
from .views import RcLoginView, RcLogoutView, profile, ChangeUserInfoView, RcPasswordChangeView, RegisterDoneView
from .views import RegisterView, user_activate, DeleteUserView


urlpatterns = [
    path('login/', RcLoginView.as_view(), name='login'),
    path('profile/', profile, name='profile'),
    path('logout/', RcLogoutView.as_view(), name='logout'),
    # --- START CRUD profile user ---
    path('create-profile/', RegisterView.as_view(), name='register'),
    path('update-profile/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('delete-profile/', DeleteUserView.as_view(), name='profile_delete'),
    # --- END CRUD profile user ---
    path('register_activate/<str:sign>/', user_activate, name='register_activate'),
    path('register_done/', RegisterDoneView.as_view(), name='register_done'),
    path('password-change/', RcPasswordChangeView.as_view(), name='password_change'),

]

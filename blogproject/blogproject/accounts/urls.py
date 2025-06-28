from django.urls import path
from .views import signup_view, profile_view, edit_profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/', profile_view, name='profile'),
    path('edit-profile/', edit_profile, name='edit_profile'),
     path('change-password/', auth_views.PasswordChangeView.as_view(
        template_name='accounts/change_password.html',
        success_url='/accounts/profile/'
    ), name='change_password'),

]

from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views as user_views

app_name = 'users'
urlpatterns = [
    path("login/", user_views.LoginView.as_view(), name="login"),
    path("signup/", user_views.SignupView.as_view(), name="signup"),
    path("profile/", user_views.UserProfileView, name="user_profile", ),
    path("profile/image-upload/", user_views.UploadProfileImageView, name="user_image_upload", ),
    path("change-password/", user_views.ChangePasswordView, name="change_password", ),
    path("delete/", user_views.DeleteAccountView, name="delete_account", ),
    path("logout/", user_views.logoutUser, name="logout"),

    re_path(r"^confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$",
            auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm", ),
    path("password-reset/complete/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete", ),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done", ),
    path("password-reset/", user_views.PasswordResetView.as_view(), name="password_reset"),

]

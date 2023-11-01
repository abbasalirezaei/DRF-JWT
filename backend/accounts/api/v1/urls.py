from django.urls import path
from . import views

app_name="accounts_v1"
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
urlpatterns = [
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),

    # password rest
    path('password/change/', views.ChangePasswordView.as_view(), name='change_password'),

    
]
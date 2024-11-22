from django.urls import path
from . import views 
from .views import register

app_name = 'user_auth'

urlpatterns = [
    path('', views.user_login, name='login'),  # Login page
    path('login/', views.user_login, name='login'),
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),  # User authentication
    path('register/', register, name='register'),  # User registration
    path('user/', views.show_user, name='user_view'),  # New user view for successful login
]

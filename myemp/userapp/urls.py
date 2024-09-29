from django.urls import path
from .views import login_view, register_view, logout_view

urlpatterns = [
    path('login/', login_view, name='login'),  # Login URL
    path('register/', register_view, name='register'),  # Registration URL
    path('logout/', logout_view, name='logout'),  # Logout URL
]





from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_profile_settings, name='testdrive'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]

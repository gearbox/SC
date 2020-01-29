from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.test_profile_settings, name='profile'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]

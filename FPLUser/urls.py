from django.urls import path
from . import views
from .views import FPLUserAPI
urlpatterns = [
    path('login', views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('api/FPLUsers',FPLUserAPI.as_view(),name='UserApi'),
    path('api/FPLUsers/<int:id>',FPLUserAPI.as_view(),name='UserAPIbyid'),
]
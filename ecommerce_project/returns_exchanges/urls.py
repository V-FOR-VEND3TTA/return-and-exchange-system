from django.urls import path
from .views import signup, user_login, user_logout, dashboard, return_exchange_request

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('', dashboard, name='dashboard'),
    path('return_exchange_request/', return_exchange_request, name='return_exchange_request'),
]
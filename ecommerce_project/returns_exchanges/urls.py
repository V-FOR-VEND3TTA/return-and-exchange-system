from django.urls import path
from .views import signup, user_login, dashboard, return_exchange_request

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    # path('logout/', views.user_logout, name='logout'),
    path('', dashboard, name='dashboard'),
    path('return_exchange_request/', return_exchange_request, name='return_exchange_request'),
]
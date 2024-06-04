from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    # path('logout/', views.user_logout, name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('return_exchange_request/<int:item_id>/', views.return_exchange_request, name='returns'),
]
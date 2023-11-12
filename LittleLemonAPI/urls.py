from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('menu', views.MenuItemView.as_view(), name='menu'),
    path('menu/category', views.CategoryView.as_view()),
    path('menu/<int:pk>', views.SingleItemView.as_view()),
    path('message/', views.msg, name='msg'),
    path('api-token-auth/', obtain_auth_token),
    path('groups/manager/users/', views.ManagerUsersView.as_view()),
    path('groups/manager/users/<int:pk>/', views.ManagerSingleUserView.as_view()),
    path('groups/delivery-crew/users/', views.DeliveryCrewManagement.as_view()),
    path('groups/delivery-crew/users/<int:pk>/', views.Delivery_crew_management_single_view.as_view()),
    path('cart/menu-items/', views.Customer_Cart.as_view()),
    path('orders/', views.OrdersView.as_view()),
    path('orders/<int:pk>/', views.SingleOrderView.as_view()),
]
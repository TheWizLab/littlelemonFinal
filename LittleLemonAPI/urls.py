from django.urls import path
from . import views

urlpatterns = [
    path('categories', views.CategoriesView.as_view(), name="category"),
    path('category/<int:pk>', views.CategorySingleView.as_view(), name="categories"),
    path('menu', views.MenuItemsView.as_view(), name="menu_items"),
    path('menu-items/<int:pk>', views.MenuItemsSingleView.as_view(), name="single_menu_item"),
    path('groups/manager/users', views.ManagerListView.as_view(), name="managers"),
    path('cart/menu-items', views.CartMenu.as_view(), name="cart-menu"),
    path('order', views.OrderListView.as_view(), name= "order"),
    path('groups', views.GroupListCreate.as_view(), name='groups'),
    path('groups/<int:pk>', views.GroupSingle.as_view(), name='groups')
]
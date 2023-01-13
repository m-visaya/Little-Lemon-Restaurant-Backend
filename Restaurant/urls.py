from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='home'),
    path('bookings', views.BookingViewSet.as_view(), name='booking'),
    path('api-token-auth/', obtain_auth_token),
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
]

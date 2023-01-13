from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Booking, MenuItem
from .serializers import BookingSerializer, MenuSerializer

class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookingViewSet(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

def index(request):
    return render(request, 'index.html', {})


from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import BookingSerializer
from .models import Booking


@api_view(['GET'])
def booking_list(request):
    bookings=Booking.objects.all()
    serializer=BookingSerializer(bookings, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['POST'])
def booking_create(request):
    serializer=BookingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_booking(request, pk):
    booking=get_object_or_404(Booking, pk=pk)
    if request.user != booking.user and not request.user.is_superuser:
        return Response({"message": "You don't have the right to update this booking"}, status=status.HTTP_403_FORBIDDEN)
    serializer=BookingSerializer(booking, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response( serializer.data, status=status.HTTP_200_OK)
    return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_booking(request,pk):
    booking=get_object_or_404(Booking,pk=pk)
    if request.user != booking.user and not request.user.is_superuser:
        return Response({"message": "you can't delete this booking"}, status=status.HTTP_403_FORBIDDEN)
    booking.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
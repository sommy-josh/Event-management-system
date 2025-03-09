from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from .models import Event
from .serializers import EventSerializer
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def event_list(request):
    events=Event.objects.all()
    serializer=EventSerializer(events,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['POST'])
def event_create(request):
    serializer=EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors)


@api_view(['PUT'])
def update_event(request,pk):
    event=get_object_or_404(Event,pk=pk)
    serializer=EventSerializer(event, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"Event updated successfully","data": serializer.data}, status=status.HTTP_200_OK)
    return Response({"message":"Validation Failed", "errors":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_event(request,pk):
        event=get_object_or_404(Event, pk=pk)
        if request.user != event.user and not request.user.is_superuser:
            return Response({"message": "you are not authorized to delete this event"}, status=status.HTTP_403_FORBIDDEN)
        event.delete()
        return Response({"message": "Event deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

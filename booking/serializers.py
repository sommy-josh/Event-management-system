from rest_framework import serializers
from .models import Booking,Event
from django.contrib.auth.models import User


class BookingSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field="username"
    )
    event = serializers.SlugRelatedField(
        queryset=Event.objects.all(), slug_field="name"
    )

    class Meta:
        model = Booking
        fields = ["user", "event", "created_at", "status"]


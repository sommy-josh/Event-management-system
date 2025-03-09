from django.db import models
from django.contrib.auth.models import User
from event.models import Event

# Create your models here.
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20, choices=[("pending", "Pending"), ("confirmed", "Confirmed"), ("canceled", "Canceled")], default="pending"
    )

    def __str__(self):
        return f"{self.user.username} - {self.event.name}"
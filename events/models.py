from django.contrib.auth.models import User
from django.db import models

# Create your models here.
CHOICES = (
    (True, "No more seats"),
    (False, "Seats still available")
)

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_time = models.DateTimeField()
    owner = models.ForeignKey(User, related_name='authored_events')
    price = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=6)
    capacity = models.PositiveSmallIntegerField(default=355)
    sold_out = models.BooleanField(choices=CHOICES, default=False)

    def __str__(self):
        return self.name

from django.db import models
from django.contrib.auth.models import User

def get_default_user():
    return User.objects.first()  # Replace with logic to fetch the desired default user

class Booking(models.Model):
    STATUS_CHOICES = [
        ('solar_panel', 'Solar Panel'),
        ('heat_pump', 'Heat Pump'),
        ('solar_farm', 'Solar Farm'),
        ('home_energy_solutions', 'Home Energy Solutions'),
        ('windmill', 'Windmill'),
        ('electric_charging_system', 'Electric Charging System')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings", default=get_default_user)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    enquiry = models.TextField()
    product = models.CharField(max_length=30, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"
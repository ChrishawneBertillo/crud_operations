from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from datetime import timedelta



class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  
    customer_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True, null=True)  

    def __str__(self):
        return self.customer_name

class Bike(models.Model):
    name = models.CharField(max_length=100)
    model_year = models.IntegerField()
    availability = models.BooleanField(default=True)
    price_per_day = models.DecimalField(max_digits=6, decimal_places=2)
    details = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='bike_images/', blank=True, null=True)

    def __str__(self):
        return f'{self.name} ({self.model_year})'
    

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('completed', 'Completed'),
    ]
    
    customer_name = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='bookings')
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE, related_name='bookings')
    booking_date = models.DateField(default=timezone.now)
    days_booked = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    due_date = models.DateField(editable=False, null=True, blank=True)  
    def save(self, *args, **kwargs):
       
        if self.customer_name and self.phone_number:
            user = kwargs.pop('user', None)  
            customer, created = Customer.objects.get_or_create(
                customer_name=self.customer_name,
                phone_number=self.phone_number,
                user=user  
            )
            self.customer = customer  

        # Calculate total price
        if self.bike and self.days_booked:
            self.total_price = self.days_booked * self.bike.price_per_day
        else:
            self.total_price = 0

        if self.booking_date and self.days_booked:
            self.due_date = self.booking_date + timedelta(days=self.days_booked)
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Booking by {self.customer} for {self.bike} (Status: {self.status})'
    
class Maintenance(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE, related_name='maintenance_records')
    maintenance_date = models.DateField()
    description = models.CharField(max_length=200)

    def __str__(self):
        return f'Maintenance on {self.bike} - {self.maintenance_date}'


class Feedback(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1) 
    text = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user} on {self.bike}' 
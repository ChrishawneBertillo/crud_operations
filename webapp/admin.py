from django.contrib import admin
from .models import Customer, Bike, Booking, Maintenance, Feedback

admin.site.register(Customer)
admin.site.register(Bike)
admin.site.register(Booking)
admin.site.register(Maintenance)
admin.site.register(Feedback)


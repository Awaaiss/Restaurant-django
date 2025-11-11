from django.contrib import admin
from .models import MenuItem, ContactMessage, Reservation

admin.site.register(MenuItem)
admin.site.register(ContactMessage)
admin.site.register(Reservation)
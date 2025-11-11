from django.db import models

# Create your models here.


# 1. Menu Item model
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    picture = models.ImageField(upload_to="menu_pictures/", blank=True, null=True)
    is_available = models.BooleanField(default=True)   # <-- add this




    def __str__(self):
        return self.name


class Order(models.Model):
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
                return f"Order for {self.item.name} by {self.customer_name}"

# 2. Contact Message model
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"


# 3. Reservation model
class Reservation(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    people = models.PositiveIntegerField()
    message = models.TextField(blank=True)

    def __str__(self):
        return f"Reservation for {self.name} on {self.date} at {self.time}"

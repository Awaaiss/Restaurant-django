from django.shortcuts import render, get_object_or_404
from .forms import ContactForm, ReservationForm, OrderForm
from .models import MenuItem, Order

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the base_app index.")
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact.html', {'form': ContactForm(), 'success': True})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
def reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'reservation.html', {'form': ReservationForm(), 'success': True})
    else:
        form = ReservationForm()
    return render(request, 'reservation.html', {'form': form})
def menu(request):
    items = MenuItem.objects.filter(is_available=True)  # Only show available items
    return render(request, 'menu.html', {'items': items})


def order_item(request , item_id):
    item = get_object_or_404(MenuItem, id=item_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.item = item
            order.save()
            return render(request, 'order_success.html', {'item': item})
    else:
        form = OrderForm()
    return render(request, 'order_item.html', {'form': form, 'item': item})
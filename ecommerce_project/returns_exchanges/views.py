from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm, ReturnExchangeForm
from .models import Order, ReturnExchangeRequest, OrderItem

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            auth_login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'returns_exchanges/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'returns_exchanges/login.html', {'form': form})

@login_required
def dashboard(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'returns_exchanges/dashboard.html', {'orders': orders})

@login_required
def return_exchange_request(request, item_id):
    order_item = OrderItem.objects.get(id=item_id)
    if request.method == 'POST':
        form = ReturnExchangeForm(request.POST)
        if form.is_valid():
            return_exchange = form.save(commit=False)
            return_exchange.order_item = order_item
            return_exchange.save()
            return redirect('dashboard')
    else:
        form = ReturnExchangeForm()
    return render(request, 'returns_exchanges/return_exchange_request.html', {'form': form, 'order_item': order_item})

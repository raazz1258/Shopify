from django.shortcuts import render, redirect
from django.contrib.auth import logout
from item.models import Category, Item
from .form import SignupForm
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    user = User.objects.all()

    return render(request, 'index.html', {
        'categories': categories,
        'items': items,
    })

def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'register.html', {
        'form': form
    })

def logout_view(request):
    logout(request)
    return redirect('/')
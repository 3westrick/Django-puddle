from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from item.models import Item
from item.models import Category
from django.contrib import messages
from .forms import SignUpForm


# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[:6]
    categories = Category.objects.all()[:6]
    return render(request, 'core/index.html', {
        'items': items,
        'categories': categories,
    })


def contact(request):
    return render(request, 'core/contact.html', {})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # auth and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully Registered!")
                return redirect("index")
            else:
                messages.error(request, "There was an error logging in, pls try again")
                return redirect("index")
    else:
        form = SignUpForm()
        return render(request, 'core/signup.html', {'form': form})
    return render(request, 'core/signup.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, "You have logged out.")
    return redirect("index")

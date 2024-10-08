from django.shortcuts import render, redirect
import random
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from comments.models import Comment
from contact.models import ContactEntry

from .forms import SignUpForm

def home_view(request):
    if request.user.is_authenticated:
        return user_dashboard_view(request)
    else:
        context = {
            'name': 'justin mitchel',
            'email': 'codingforentrepreneurs@gmail.com'
        }
        return render(request, 'home.html', context)

def about_view(request):
    context = {
        'title': 'About Us',
        'description': 'We are a team of passionate developers working on the Cursor Django project.'
    }
    return render(request, 'about.html', context)

# Add these new views
def contact_view(request):
    context = {
        'title': 'Contact Us',
        'description': 'Get in touch with us for any inquiries.'
    }
    return render(request, 'contact.html', context)

def pricing_view(request):
    context = {
        'title': 'Pricing',
        'description': 'Check out our competitive pricing plans.'
    }
    return render(request, 'pricing.html', context)

def products_view(request):
    context = {
        'title': 'Our Products',
        'description': 'Explore our range of products and services.'
    }
    return render(request, 'products.html', context)

def tech_stack(request):
    return render(request, 'tech_stack.html')


def product_detail_view(request, product_id):
    # In a real application, you would fetch the product from a database
    # For this example, we'll use a dummy product
    product = {
        'id': product_id,
        'name': f'Product {product_id}',
        'description': f'This is the detailed description for Product {product_id}.',
        'price': round(product_id * 10 + random.uniform(0.99, 9.99), 2)
    }
    
    context = {
        'product': product
    }
    return render(request, 'product_detail.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('home')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



@login_required
def user_dashboard_view(request):
    user = request.user
    
    # Fetch comments and contact entries for the user
    comments = Comment.objects.filter(user=user)
    contact_entries = ContactEntry.objects.filter(user=user)
    
    # Combine querysets
    combined_data = list(comments) + list(contact_entries)
    # Sort combined data by creation date
    combined_data.sort(key=lambda x: x.created_at, reverse=True)
    
    # Get counts
    comments_count = comments.count()
    contact_entries_count = contact_entries.count()
    
    context = {
        'user_data': combined_data,
        'comments_count': comments_count,
        'contact_entries_count': contact_entries_count,
    }
    
    return render(request, 'dashboard/user_dashboard.html', context)
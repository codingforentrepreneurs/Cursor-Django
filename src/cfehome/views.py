from django.shortcuts import render
import random


def home_view(request):
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

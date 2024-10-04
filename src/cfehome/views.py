from django.shortcuts import render

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
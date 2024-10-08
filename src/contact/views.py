from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

# Create your views here.

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_entry = form.save(commit=False)
            if request.user.is_authenticated:
                contact_entry.user = request.user
            contact_entry.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')  # Redirect to a 'thank you' page or back to the contact form
    else:
        form = ContactForm()
    
    return render(request, 'contact/contact_form.html', {'form': form})

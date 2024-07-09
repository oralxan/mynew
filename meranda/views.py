from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Category, Healthy, Sport, Design
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings


class CategoryListView(ListView):
    model = Category
    template_name = 'meranda/category_list.html'


class HealthyListView(ListView):
    model = Healthy
    template_name = 'meranda/healthy_list.html'

class SportListView(ListView):
    model = Sport
    template_name = 'meranda/sport_list.html'

class HealthyDetailView(DetailView):
    model = Healthy
    template_name = 'meranda/healthy_detail.html'

class SportDetailView(DetailView):
    model = Sport
    template_name = 'meranda/sport_detail.html'

class DesignListView(ListView):
    model = Design
    template_name = 'meranda/design_list.html'

class DesignDetailView(DetailView):
    model = Design
    template_name = 'meranda/design_detail.html'



from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            send_mail(
                f'Message from {name}',
                message,
                email,
                ['orallxannajmatdinova@gmail.com'],  
            )
            
            return redirect('success')  
    else:
        form = ContactForm()

    return render(request, 'meranda/contact.html', {'form': form})


def contact_success_view(request):
    return render(request, 'meranda/success.html')






from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Deal


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def deal_index(request):
    deals = Deal.objects.all()
    return render(request, 'deals/index.html', {'deals': deals})

def deal_detail(request, deal_id):
    deal = Deal.objects.get(id=deal_id)
    return render(request, 'deals/detail.html', {'deal': deal})

class DealCreate(CreateView):
    model = Deal 
    fields = '__all__'

class DealUpdate(UpdateView):
    model = Deal
    fields = ['industry', 'asking_price', 'revenue', 'sde', 'status', 'notes']

class DealDelete(DeleteView):
    model = Deal
    success_url = '/deals/'

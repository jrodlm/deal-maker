from django.shortcuts import render
from .models import Deal


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def deal_index(request):
    deals = Deal.objects.all()
    return render(request, 'deals/index.html', {'deals': deals})

def deal_detail(request, cat_id):
    deal = Deal.objects.get(id=deal_id)
    return render(request, 'deals/detail.html', {'deal': deal})

# class Deal:
#     def __init__(self, company_name, industry, asking_price, revenue, sde, status, notes, created_on):
#         self.company_name = company_name
#         self.industry = industry
#         self.asking_price = asking_price
#         self.revenue = revenue
#         self.sde = sde
#         self.status = status
#         self.notes = notes
#         self.created_on = created_on

# deals = [
#     Deal('Acme', 'B2B', '$1,420,000', '$725,000', '$250,000',  'new', 'n/a','TBD'),
#     Deal('AI Hub', 'SaaS', '$2,212,000', '$1,233,000', '$350,000', 'expressed interest', 'n/a', 'TBD'),
#     Deal('Service Masters', 'Industrial Services', '$1,489,000', '$999,000','$450,000','under loi', 'n/a','TBD'),
#     Deal('Plug It', 'Plumbing', '$1,745,000','$1,410,000', '$550,000','expressed interest','n/a','TBD')
# ]

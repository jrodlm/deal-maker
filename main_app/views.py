from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Deal
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

@login_required
def deal_index(request):
    deals = Deal.objects.filter(user=request.user)
    return render(request, 'deals/index.html', {'deals': deals})

@login_required
def deal_detail(request, deal_id):
    deal = Deal.objects.get(id=deal_id)
    return render(request, 'deals/detail.html', {'deal': deal})

class DealCreate(LoginRequiredMixin, CreateView):
    model = Deal 
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)

class DealUpdate(LoginRequiredMixin, UpdateView):
    model = Deal
    fields = ['industry', 'asking_price', 'revenue', 'sde', 'status', 'notes']

class DealDelete(LoginRequiredMixin, DeleteView):
    model = Deal
    success_url = '/deals/'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('deal-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
  

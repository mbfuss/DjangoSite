from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, login

from news.models import Articles

def layout(request):
    cats = Articles.objects.all()
    context = {
        'cats': cats,
        'cat_selected': 0,
    }
    return render(request,'news/news_home.html',context)

def index(request):
    
    context = {
        'title': 'Главная страница',
    }
    return render(request,'main/index.html',context )

def about(request):
    return render(request, 'main/about.html')

class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'main/register.html' # ссылка нашаблон
    success_url = reverse_lazy('login') # переадресация при успешной регистрации

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'main/login.html'
    #Если данные верны, то 'home'
    def get_success_url(self):
        return reverse_lazy('home')
    
def logout_user(request):
    logout(request)
    return redirect('login')



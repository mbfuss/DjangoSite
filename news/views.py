from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


# Показ новостей 5 шт
def news_home(request):
    news = Articles.objects.order_by('-date')[:5]
    return render(request, 'news/news_home.html', {'news':news})

class NewsDetalView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticlesForm

class NewsDeleteView(DeleteView):
    model = Articles
    template_name = 'news/news-delete.html'
    success_url = '/news/'

# Отправка/обработка формы в бд
def create(request):
    error = ''
    # Нажимаем добавить -> выполняется проверка
    # Отправка\проверка отправеки с помощью метода post (create.html/ <form method="post">)
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        # Если данные корректно заполнены, то сохранить в бд
        if form.is_valid(): 
            form.save()
            return redirect('news_home')
        else:
            error = 'ERROR'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html',data)

def layout(request):
    cats = Articles.objects.all()
    context = {
        'cats': cats,
        'cat_selected': 0,
    }
    return render(request,'news/news_home.html',context)

def show_category(request, cat_id):
    return HttpResponse(f"Отображение категории с id = {id}")

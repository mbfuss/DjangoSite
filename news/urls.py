#файл для отслеживания url адресов
from django.urls import path
from . import views
urlpatterns = [
    path('', views.news_home, name ='news_home'),  #  отслеживаем пустую строку, т.к. когда пользователь вводит /news мы сиюда автоматически перебрасываемся ч\з mysite.urls
    path('create', views.create, name ='create'),
    path('<int:pk>', views.NewsDetalView.as_view(), name ='news-detail'), # <int:pk> динамический параметр
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name ='news-update'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name ='news-delete'),
    path('category/<int:cat_id>/',views.show_category, name ='category'),
]

#файл для отслеживания url адресов
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls), # при переходе /admin/... вызывается admin.site.urls
    path('', include('main.urls')), #если пользователь переходит на гл. url, то подключаем файл main.urls
    path('news/', include('news.urls')) # если пользователь переходит на /news/..., то он будет обрабатываться в news/urls.py
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # подключение static файлов

#Если например пользователь введет /about, то он будет обрабатываться в main.urls
#файл для отслеживания url адресов
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name ='home'),  #  при переходе на гл. страницу -- '', вызываем метод views.index
    path('about/',views.about, name ='about'), # при переходе на url about вызываем метод views.about
    path('register/', views.RegisterUser.as_view(), name ='register'),
    path('login/',views.LoginUser.as_view(), name ='login'),
    path('logout/',views.logout_user, name ='logout'),
]

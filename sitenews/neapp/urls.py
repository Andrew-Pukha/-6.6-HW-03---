from django.contrib import admin
from django.urls import path, re_path, register_converter
from neapp import views
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.news_page, name='home'),                                     #http://127.0.0.1:8000 - Страница приложения neapp со списком материала.
    path('cats/<int:cat_id>/', views.categories, name='cats_id'),               #http://127.0.0.1:8000/cats/<int>/
    path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats'),       #http://127.0.0.1:8000/cats/<slug>/

    path('archive/<year4:year>/', views.archive, name='archive'),                #http://127.0.0.1:8000/archive/<year>/
    path('about/', views.about, name='about'),
    path('post/<slug:post_slug>/', views.show_post, name='post'),                #http://127.0.0.1:8000/post/<int>/ -  #13. Создаём кнопку "Читать пост", которая будет работать и открывать Пост. Сначала прописываем маршрут.
    #13 Данные маршруты являются маршрутами Главного меню. Сделаем кнопки Главного меню живыми, сначала пишем маршрут:
    path('addpage/', views.addpage, name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('category/<slug:cat_slug>/', views.show_category, name='category'),        #16. Добавим URL-адреса для категорий.

]


from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string    #9. Шаблоны

from .models import Post, Category

#13. Коллекция Главного меню (делаем кнопки ГМ кликабельными). Маршруты, функции представления и шаблоны уже прописаны:
menu = [{'title': "О сайте", 'url_name': 'about'},               #13. 'title' - это название пункта Главного Меню, а 'url_name' - название машрута пункта Главного Меню.
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]







#Страница со списком ВСЕХ новостей:
def news_page(request):
    posts = Post.published.all()
    data = {
        'title': 'Главная страница',                                                #10. Переменные 'title' и 'menu' подставились в шаблон.
        'menu': menu,
        'posts': posts,
        'cat_selected': 0,
    }
    return render(request, 'neapp/news_page.html', context=data)        #9. Шаблоны.








#9. Страница О САЙТЕ новостей:
def about(request):
    data = {
        'title': 'О сайте',  #10. Переменные 'title' и 'menu' подставились в шаблон.
        'menu': menu,        #14. Список menu был добавлен на страницу about/.
    }
    return render(request, 'neapp/about.html', context=data)






#13. Создаём кнопку "Читать пост", которая будет работать и открывать Пост. После написания маршрута(post/), написали функцию представления show_post().
def show_post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected': 1,
    }
    return render(request, 'neapp/post.html', context=data)


#16. Функция представления show_category() будет показывать
def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Post.published.filter(cat_id=category.pk)
    data = {
        'title': f'Рубрика: {category.name}',             #10. Переменные 'title' и 'menu' подставились в шаблон.
        'menu': menu,
        'posts': posts,
        'cat_selected': category.pk,
    }
    return render(request, 'neapp/news_page.html', context=data)







#5. Страница со списком КАТЕГОРИЙ новостей (выводится по запросу: #http://127.0.0.1:8000/cats/<int>/):
def categories(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p >id:{cat_id}</p>")

#6. Страница со списком КАТЕГОРИЙ новостей (#http://127.0.0.1:8000/cats/<slug>/):
def categories_by_slug(request, cat_slug):
    print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p >slug:{ cat_slug }</p>")





#7. Страница АРХИВА новостей:
def archive(request, year):
    if year > 2025:
        return redirect('/')                                        #8. redirect - перенаправление с кодом 302.
    return HttpResponse(f"<h1>Архив по годам</h1><p >{year}</p>")






#13. Описываем функции представления кнопок Главного меню (делаем кнопки ГМ кликабельными). Маршруты уже прописаны:
def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")





def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')











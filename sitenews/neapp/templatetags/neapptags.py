
from django import template
import neapp.views as views
from neapp.models import Category

register = template.Library()

#-- Второй тип пользовательских тегов – включающий тег,
#-- позволяет дополнительно формировать свой собственный шаблон на основе
#-- некоторых данных и возвращать фрагмент HTML-страницы.


@register.inclusion_tag('neapp/list_categories.html')
def show_categories(cat_selected_id=0):
    cats = Category.objects.all()
    return {"cats": cats, "cat_selected": cat_selected_id}
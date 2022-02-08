from django.db.models import Count
from django.core.cache import cache
from .models import *

menu = []

class DataMixin:
    paginate_by = 3
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        # берёт данные из кэша(если они есть)
        # cats = cache.get('cats')
        # если кэша нету то мы его создаём. set-устанавливает что откуда и на сколько брать
        # 'cats'-название ключа который мы сами придумали. get- просто берёт данные
        # if not cats:
        #     cats = Category.objects.all()
        #     cache.set('cats', cats, 60)


        # ТЕПЕРЬ ЧЕРЕЗ ЭТО ИМЯ cats МЫ МОЖЕМ ОБРАЩАТЬСЯ В ШАБЛОНАХ И ПЕРЕБИРАТЬ
        # ЕГО СОДЕРЖИМОЕ
        context['cats'] = cats
        context['menu'] = menu
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context

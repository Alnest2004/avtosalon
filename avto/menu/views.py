from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView

from menu.forms import RegisterUserForm, LoginUserForm, AddPostForm
from menu.models import *
from menu.utils import *


class Index(DataMixin, ListView):
    model = Cars
    template_name = 'menu/index.html'
    context_object_name = 'list_cars'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="CarShowroom", number=0)
        context = dict(list(context.items()) + list(c_def.items()))
        return context
    #select_related - Так же он работает для соединения ForeignKey.
    # В то время как prefetch_related - для связей manytomany.
    # Данный метод позволяет забирать в одном запросе ещё
    # и дополнительные объекты из других таблиц. Это позволит объединить
    # множество запросов в один и ускорить выборку, а также уменьшить накладные
    # расходы на подключение к базе данных, посокольку количество подключений
    # уже очень сильно уменьшится.
    def get_queryset(self, **kwargs):
        return Cars.objects.all()


class CarsCategory(DataMixin, ListView):
    model = Cars
    template_name = 'menu/index.html'
    context_object_name = 'list_cars'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title="Категория - " + c.name, number=c.pk)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    # Этот метод используется для возвращения того что должно быть прочитано
    # из модели Cars. Получается что теперь мы будем читать не все записи, а
    # только те для которых условие верно.
    def get_queryset(self):
        # Выбираем записи из таблицы те которым соответствуют категории по указанному
        # слагу. .kwargs['cat_slug'] - получаем все параметры нашего маршрута
        # (в url который в данном случаи у нас он один и это cat_slug). В частности
        # переменную cat_slug которую мы прописали в urls.py. cat__slug - слаг категории
        # cat__slug - означает что мы обращаемся к полю slug вот этой таблицы cat,
        # связанной с этой текущей записью
        # ['cat_slug'] - ЭТО ЗНАЧЕНИЕ ИЗ URL
        return Cars.objects.filter(cat__slug=self.kwargs['cat_slug'])


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')



class CarSlug(DataMixin, DetailView):
    model = Cars
    template_name = 'menu/test.html'
    # УКАЗЫВАЕМ ИМЯ которое указанно в urls.py которое мы и будем использовать
    # без этого детальное отображение элементов невозможно
    slug_url_kwarg = 'car_slug'
    context_object_name = 'test'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # тут заголовок формируется на основе публикации
        c_def = self.get_user_context(title=context['test'])
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class RegisterUser(DataMixin, CreateView):
    # RegisterUserForm - наша собственная форма в forms.py
    form_class = RegisterUserForm
    template_name = 'menu/register.html'
    # success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация", ssilka='register')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        # сохроняем форму в базу данных
        user = form.save()
        # login - функция джанго которая авторизовывает пользователя
        login(self.request, user)
        return redirect('home')

class LoginUser(DataMixin, LoginView):
    # RegisterUserForm - наша собственная форма в forms.py
    form_class = LoginUserForm
    template_name = 'menu/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Логин", ssilka='login')
        return dict(list(context.items())+list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')


class AboutSite(DataMixin, FormView):
    template_name = 'menu/about.html'
    form_class = FormView

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='О нас', ssilka='about')
        return dict(list(context.items())+list(c_def.items()))

# LoginRequiredMixin запрещает доступ не зарегестрированным пользователям у класса
class AddPage(LoginRequiredMixin , DataMixin, CreateView):
    # AddPostForm - класс формы который будет подключаться к этому классу вида(form_class)
    # AddPostForm - мы создаём сами в forms.py
    form_class = AddPostForm
    template_name = 'menu/addcars.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = "Добавление статьи", ssilka='addcars')
        context = dict(list(context.items())+list(c_def.items()))
        return context

    # def get_queryset(self):
    #     return Cars.objects.filter(borrower=self.request.user)



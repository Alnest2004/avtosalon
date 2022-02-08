from django.test import TestCase

from menu.forms import *
from menu.models import Cars, Category
from django.urls import reverse
from django.contrib.auth.models import User


class CarsListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.cat = Category(name='Дорогой', slug='dorogoi')
        cls.cat.save()
        number_of_Cars = 9
        for cars_num in range(number_of_Cars):
            Cars.objects.create(cat=cls.cat, photo=' ', model='Lamborgini %s' % cars_num,
                                slug='test_car_1_%s' % cars_num, text='тестовый текст 1 ! %s' % cars_num)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('category', kwargs={'cat_slug': self.cat.slug}))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('category', kwargs={'cat_slug': self.cat.slug}))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'menu/index.html')

    def test_pagination_is_three(self):
        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertEqual(len(resp.context['list_cars']), 3)

    def test_lists_all_Cars(self):
        # Тут мы проверяем последнюю страницу, проверяем взяла ли она оставшиеся статьи
        # берём получается последнюю страницу и считаем сколько элементов на этой странице
        # и проверяем совпадает ли это число с оставшиемися постами. Например если бы
        # у нас на каждой странице было бы по 4 поста, а всего 9, тогда мы должны были бы
        # проверить что на последней странице 1 пост. То есть в последней строчке поменять на цифру 1
        resp = self.client.get(reverse('home') + '?page=3')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertEqual(len(resp.context['list_cars']), 3)


class AddPageListViewTest(TestCase):
    def setUp(self):
        # Создание двух пользователей
        test_user1 = User.objects.create_user(username='testuser1', password='12345')
        test_user1.save()
        test_user2 = User.objects.create_user(username='testuser2', password='12345')
        test_user2.save()


        # Создание 10 объектов Cars
        number_of_cars_copies = 10
        for car_copy in range(number_of_cars_copies):
            # Создание категории про машину
            test_category = Category.objects.create(name='Бюджетные_%s' % car_copy, slug='byudzhetnye_%s' % car_copy)
            Cars.objects.create(cat=test_category,photo=" ", model='Ferrari', slug='ferrari_%s' % car_copy,
                                text='Тестовый текст для машины Ferrari')

    # def test_redirect_if_not_logged_in(self):
    #     resp = self.client.get(reverse('login'))
    #     self.assertRedirects(resp, 'home')

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='12345')
        resp = self.client.get(reverse('add_page'))

        # Проверка что пользователь залогинился
        self.assertEqual(str(resp.context['user']), 'testuser1')
        # Проверка ответа на запрос
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'menu/addcars.html')




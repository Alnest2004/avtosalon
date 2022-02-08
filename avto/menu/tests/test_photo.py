from django.test import TestCase
from menu.models import *
from django.core.files.uploadedfile import SimpleUploadedFile


class BaseModelTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super(BaseModelTestCase, cls).setUpClass()
        cls.cat = Category(name='Дорогой', slug='dorogoi')
        cls.cat.save()
        cls.first_car = Cars(cat=cls.cat,photo='755681010440759.jpg', model='Test car 1', slug='test_car_1', text='тестовый текст 1 !')
        cls.first_car.save()


    def test_html_photo(self):
        newPhoto = SimpleUploadedFile(name='755681010440759.jpg', content=open('media/photos/2021/12/17/755681010440759.jpg', 'rb').read(), content_type='image/jpeg')
        self.assertEqual(self.first_car.photo, newPhoto)
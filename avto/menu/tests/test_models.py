from django.test import TestCase
from menu.models import *
from django.core.files.uploadedfile import SimpleUploadedFile


class BaseModelTestCase(TestCase):

    # cls — это стандартное имя первого аргумента методов класса.
    # clsподразумевает, что метод принадлежит классу, в то время как
    # self подразумевает, что метод связан с экземпляром класса,
    @classmethod
    def setUpClass(cls):
        super(BaseModelTestCase, cls).setUpClass()
        cls.cat = Category(name='Дорогой', slug='dorogoi')
        cls.cat.save()
        cls.first_car = Cars(cat=cls.cat, model='Test car 1', slug='test_car_1', text='тестовый текст 1 !')
        cls.first_car.save()

    def test_model_length(self):
        max_length = self.first_car._meta.get_field('model').max_length
        self.assertEquals(max_length, 30) # Если тут указать вместо 30
        # больше или меньше, то будет ошибка так как число не соответствует
        # числу которое написанно в models.py(max_length=30).

    def test_html_photo(self):
        self.first_car.photo = SimpleUploadedFile(name='755681010440759.jpg', content=open('media/photos/2021/12/17/755681010440759.jpg', 'rb').read(), content_type='image/jpeg')
        self.assertEqual(self.first_car.photo, '755681010440759.jpg')



class CategoryModelTestCase(BaseModelTestCase):
    def test_created_properly(self):
        self.assertEqual(self.cat.name, 'Дорогой')
        self.assertEqual(True, self.first_car in self.cat.cars_set.all())


    def test_absolute_url(self):
        self.assertEqual(self.cat.get_absolute_url(), reverse('category', kwargs={'cat_slug': self.cat.slug}))

class CarsModelTestCase(BaseModelTestCase):
    def test_created_properly(self):
        self.assertEqual(self.first_car.model, 'Test car 1')

    def test_absolute_url(self):
        self.assertEqual(self.first_car.get_absolute_url(), reverse('post', kwargs={'car_slug': self.first_car.slug}))




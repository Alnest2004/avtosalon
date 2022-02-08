# python manage.py test catalog.tests   # Run the specified module
# python manage.py test catalog.tests.test_forms  # Run the specified module
# python manage.py test catalog.tests.test_forms.YourTestClass # Run the specified class
# python manage.py test menu.tests.test_forms.RegisterUserFormTest.test_username_field_label  # Run the specified method

from django.test import TestCase

# Создайте ваши тесты здесь

from menu.forms import *
from menu.models import Cars



class RegisterUserFormTest(TestCase):


    def test_username_field_label(self):
        form = RegisterUserForm()
        self.assertTrue(form.fields['username'].label == None or form.fields['username'].label == 'Логин')

    # def test_username_field_widget(self):
    #     form = RegisterUserForm()
    #     print("---------")
    #     print(form.fields['username'].widget)
    #     self.assertTrue(form.fields['username'].attrs == None or form.fields['username'].attrs == "'class': 'form-input'")

    def test_meta(self):
        form = RegisterUserForm()
        ordering = form._meta.fields
        self.assertEqual(ordering, ('username', 'email', 'password1', 'password2'))


class AddPostFormTest(TestCase):
    def test_meta(self):
        form = AddPostForm
        ord2 = form._meta.fields
        self.assertEqual(ord2, ['model', 'slug', 'text', 'photo', 'cat'])





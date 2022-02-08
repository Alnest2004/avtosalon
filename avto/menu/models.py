from django.db import models
from django.template.defaultfilters import truncatechars
from django.urls import reverse


class Cars(models.Model):
    model = models.CharField(max_length=30,)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    text = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", null=True)
    cat = models.ForeignKey('Category', null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.model

    def get_absolute_url(self):
        return reverse('post', kwargs={'car_slug': self.slug})

    def get_html_photo(self):
        if self.photo:
            from django.utils.safestring import mark_safe
            return mark_safe(f"<img src='{self.photo.url}' width=150>")

    get_html_photo.short_description = "Миниатюра"

    def short_text(self):
        return truncatechars(self.text, 50)


class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

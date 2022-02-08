from django.urls import path, include
from django.views.decorators.cache import cache_page
from menu.views import *

# name указывается что бы к нему обращаться в шаблонах. Если например нам нужно
# будет изменить путь, то изменить придётся только тут в path('')
# name='post' - также влияет на то как будут называться пути в models.py и тд, скорее всего и везде тоже
urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('category/<slug:cat_slug>/', CarsCategory.as_view(), name='category'),
    path('car/<slug:car_slug>/', CarSlug.as_view(), name='post'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    path('login/', LoginUser.as_view(), name='login'),
    path('about/', AboutSite.as_view(), name='about'),
    path('addcars/', AddPage.as_view(), name='add_page'),
]

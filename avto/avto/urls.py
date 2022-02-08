from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from avto import settings
from django.conf.urls.static import static
from menu.views import *

router = SimpleRouter()


# Использование namespace в include() позволяет включать одно и то же
# приложение несколько раз с разным пространством имен для каждого экземпляра.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('menu.urls')),
    # path('silk/', include('silk.urls', namespace='silk')),
    path('api-auth/', include('rest_framework.urls'))
]

if settings.DEBUG:
    import mimetypes

    mimetypes.add_type("application/javascript", ".js", True)

    urlpatterns = [
                      path('__debug__/', include('debug_toolbar.urls')),
                  ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = pageNotFound
from django.contrib import admin
from django.urls import path, include
from dj_rest_auth.urls import urlpatterns as up
from django.conf import settings
from django.conf.urls.static import static
up.remove(up[0])
up.remove(up[0])
up.remove(up[2])
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    path('api/', include('SAMS.urls')),
    path('login-logout-change/', include('dj_rest_auth.urls')),
    path('rpi/', include('RPi.urls')),
    path('Lecture/',include('Lecture.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

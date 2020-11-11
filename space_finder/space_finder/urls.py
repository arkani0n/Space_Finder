from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',        include('main.urls')),
    path('/search', include('search.urls')),
    path('/history', include('history.urls')),
    path('admin/', admin.site.urls),
    path('/info',include('info.urls'))
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

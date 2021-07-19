from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('beer_collector.core.urls')),
                  path('auth/', include('beer_collector.account.urls')),
                  path('profile/', include('beer_collector.collector_profile.urls')),
              ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

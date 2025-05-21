from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing_page.urls')),  # ini penting!
    path('donation/', include('donation.urls')),  # ini penting!
    path('relawan/', include('relawan.urls')),  # ini penting!
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

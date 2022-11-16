
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static


admin.site.site_header = "DesertWings Admin"
admin.site.site_title = "DesertWings Admin Portal"
admin.site.index_title = "Welcome to DesertWings Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('account.urls')),
    path('api/home/', include('package.urls')),
    path('api/booking/', include('booking.urls')),
    path('api/blog/', include('blogs.urls')),
    path('api/b2b/', include('b2b.urls')),
    path('api/visa/', include('visa.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
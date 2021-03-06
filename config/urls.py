from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

import customer

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('pages.urls', namespace='pages')),
    path('blog/', include('blog.urls', namespace='blogs')),
    path('customer/', include('customer.urls', namespace='customer')),
    path('product/', include('product.urls', namespace='product'))
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

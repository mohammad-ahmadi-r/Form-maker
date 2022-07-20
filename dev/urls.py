from django.contrib import admin
from django.urls import path , include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('', include('django.conf.urls.i18n')),
]
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('auth/' , include('atent.urls')),
    path('' , include('form.urls')),
)

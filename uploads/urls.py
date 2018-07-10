from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from core import views as core_views


urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    url(r'^uploads/simple/$', core_views.simple_upload, name='simple_upload'),
    url(r'^uploads/form/$', core_views.model_form_upload, name='model_form_upload'),
    url(r'^list/form/$', core_views.list, name='list'),
    url('contato/', core_views.contact),
    url(r'^admin/', admin.site.urls),
]


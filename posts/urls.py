from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^(?P<post_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'(?P<page_number>\d)*/*addlike/(?P<post_id>[0-9]+)/$', views.addlike),
    url(r'(?P<post_id>\d)*/*addlike_in/(?P<page_number>\d)+/$', views.addlike),
    url(r'^(?P<post_id>[0-9]+)/addcomment/$', views.addcomment),
    url(r'^page/(\d+)/$', views.index),
    url(r'^$', views.index, name='index'),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
#при получении запроса posts\ и далее все, что угодно, мы отправляемся в views.py, функция index
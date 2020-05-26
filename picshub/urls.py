from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$', views.index, name = "homepage"),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^image/(\d+)',views.image,name ='image'),
    url(r'^category/(?P<category_id>(\d+))',views.categories,name='categoryView'),
    url(r'^image/(?P<image_id>(\d+))',views.image,name='imageview')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
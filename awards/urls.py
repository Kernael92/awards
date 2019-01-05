from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$',views.index, name="index"),
    url(r'^new/project$', views.new_project, name='new-project'),
    url(r'^setting/(?P<username>[\w.@+-]+)/$', views.profile_setting, name='profile_setting'),
    url(r'^profile/(?P<username>[\w.@+-]+)/$', views.profile, name='profile'),
    url(r'^search/',views.search_project, name="search_projects"),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$',views.index, name="index"),
    url(r'^new/project$', views.new_project, name='new-project'),
    url(r'^setting$', views.profile_setting, name='edit-profile'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from rest_framework import routers
from notes.views import NoteViewSet

router = routers.DefaultRouter()
router.register(r'notes',NoteViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TaskM.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),

)

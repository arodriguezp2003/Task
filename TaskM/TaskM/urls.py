from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from rest_framework import routers
from notes.views import NoteViewSet
from alerts.views import AlertViewSet
from organizations.views import OrganizationViewSet, OrganizationUserViewSet
router = routers.DefaultRouter()
router.register(r'notes',NoteViewSet)
router.register(r'alerts',AlertViewSet)
#router.register(r'organizations',OrganizationViewSet)
#router.register(r'organizationsuser',OrganizationUserViewSet)
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TaskM.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),


)

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from rest_framework import viewsets, routers

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from twitter.models import Tweet

class TweetViewSet(viewsets.ModelViewSet):
    model = Tweet

router = routers.DefaultRouter()
router.register(r'tweets', TweetViewSet)



urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html')),

    # Examples:
    # url(r'^$', 'gdgapi.views.home', name='home'),
    # url(r'^gdgapi/', include('gdgapi.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^api/', include(router.urls)),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)

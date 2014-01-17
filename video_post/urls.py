from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'video_post.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('video_post.apps.main.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

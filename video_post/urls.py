from django.conf.urls import patterns, include, url

from django.contrib import admin
import video_post.main as main

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'video_post.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^post/', include('video_post.main.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

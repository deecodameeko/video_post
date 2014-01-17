from django.conf.urls import patterns, url

from video_post.apps.main import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^post_photo/$', views.post_photo, name='post_photo'),
    #url(r'^post_video/(?P<submission_id>\d+)/$', views.post_video, name='post_video'),
    url(r'^post_video/$', views.post_video, name='post_video'),
    url(r'^save_access_token/(?P<access_token>\w+)/$', views.save_access_token, name='save_access_token'),
)
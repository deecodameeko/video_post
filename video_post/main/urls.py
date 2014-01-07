from django.conf.urls import patterns, url

from video_post.main import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)
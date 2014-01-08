from django.conf.urls import patterns, url

from video_post.apps.main import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)
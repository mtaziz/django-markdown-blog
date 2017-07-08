from django.conf.urls import url

from posts.views import PostDetail, PostList


urlpatterns = [
    url(r'^posts/(?P<year>[0-9]{4})/(?P<pk>[0-9]+)/$', PostDetail.as_view(), name='post'),
    url(r'^tag/(?P<tag>[-\w]+)/$', PostList.as_view(), name='tag'),
    url(r'^$', PostList.as_view(), name='posts'),
]

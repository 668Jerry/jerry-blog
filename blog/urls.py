from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'article.views.create'),
    url(r'^now/', 'article.views.now'),
    url(r'^now', 'article.views.now'),
    url(r'^article/(?P<pk>[0-9]+)/$', 'article.views.detail'),
    url(r'^article/(?P<pk>[0-9]+)$', 'article.views.detail'),
    url(r'^create/$', 'article.views.create'),
    url(r'^create$', 'article.views.create'),
    url(r'.*/', 'article.views.helloWorld'),
)

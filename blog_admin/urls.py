from django.conf.urls import patterns, include, url

urlpatterns = patterns('blog_admin.views',
        url(r'^$', 'dashboard')
)

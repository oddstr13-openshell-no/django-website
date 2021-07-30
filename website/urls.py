from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic.base import RedirectView

from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^website/', include('website.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/',   include(admin.site.urls)),
    
    url(r'^paste/',   include('pastebin.urls')),
    url(r'^gallery/', include('gallery.urls')),
    url(r'^blog/',    include('blog.urls')),
    url(r'^$', RedirectView.as_view(url='/blog/', permanent=False), name='index'), # http://www.stepforth.com/blog/2008/redirects-permanent-301-vs-temporary-302/
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


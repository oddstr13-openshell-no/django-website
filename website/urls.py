from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic.base import RedirectView

from django.contrib import admin

# admin.autodiscover()

import blog.urls
import gallery.urls
import pastebin.urls

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^paste/", include(pastebin.urls)),
    url(r"^gallery/", include(gallery.urls)),
    url(r"^blog/", include(blog.urls)),
    # http://www.stepforth.com/blog/2008/redirects-permanent-301-vs-temporary-302/
    url(r"^$", RedirectView.as_view(url="/blog/", permanent=False), name="index"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

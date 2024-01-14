from django.urls import include, re_path
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic.base import RedirectView

from django.contrib import admin

# admin.autodiscover()

import blog.urls
import gallery.urls
import pastebin.urls

urlpatterns = [
    re_path(r"^admin/", admin.site.urls),
    re_path(r"^paste/", include(pastebin.urls)),
    re_path(r"^gallery/", include(gallery.urls)),
    re_path(r"^blog/", include(blog.urls)),
    # http://www.stepforth.com/blog/2008/redirects-permanent-301-vs-temporary-302/
    re_path(r"^$", RedirectView.as_view(url="/blog/", permanent=False), name="index"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

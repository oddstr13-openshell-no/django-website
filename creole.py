#!/usr/bin/python
import genshi
import creoleparser

from django.utils.html import escape

from pastebin.models import Paste
from pastebin.lib import pygmentize


def macro_paste(macro, environ, id):
    result = ""
    try:
        paste = Paste.objects.get(urlid=id)
    except Paste.DoesNotExist:
        paste = None
    if paste is not None:
        result += '<div class="inline_paste">'
        result += '<div class="inline_paste_head">Paste <code><a href="/paste/{id:s}/">{id:s}</a></code></div>'.format(
            id=id
        )
        result += pygmentize(paste.text, paste.lang.code)
        result += "</div>"
    else:
        result += "<p>Invalid paste id</p>"
    return genshi.Markup(result)


from gallery.models import Image
from sorl.thumbnail import get_thumbnail
from django.urls import reverse


def margin(im, x, y):
    # from sorl
    margin = [0, 0, 0, 0]
    ex = x - im.x
    margin[3] = ex / 2
    margin[1] = ex / 2
    if ex % 2:
        margin[1] += 1
    ey = y - im.y
    margin[0] = ey / 2
    margin[2] = ey / 2
    if ey % 2:
        margin[2] += 1
    return " ".join(["%spx" % n for n in margin])


def macro_image(macro, environ, id, caption=None):
    result = ""
    try:
        im = Image.objects.get(id=id)
    except Image.DoesNotExist:
        im = None
    if im is not None:
        th = get_thumbnail(im.image, "780x482")
        result += '<div class="blogimage" style="width:{width}px;"><a href="{url}"><img style="padding:0;" src="{image}" width="{width}" height="{height}" alt="{title}" title="{title}" /></a>{caption}</div>'.format(
            margin=margin(th, 780, 482),
            image=th.url,
            url=reverse("gallery-image", kwargs={"id": id}),
            width=th.x,
            height=th.y,
            title=im.title,
            caption=caption or im.title,
        )
    else:
        result += "<p>Invalid image id</p>"
    return genshi.Markup(result)


dialect = creoleparser.create_dialect(
    creoleparser.creole11_base,
    non_bodied_macros={
        "image": macro_image,
        "paste": macro_paste,
    },
    wiki_links_base_url=["/blog/post/", "/gallery/image/"],
    #    wiki_links_path_func=interwiki_path_test,
    interwiki_links_base_urls={
        #        'wiki' : "http://wiki.urbancraft.no/wiki/", # [[wiki:SandBox|wiki test page]]  =  <a href="http://wiki.urbancraft.no/SandBox">wiki test page</a>
        "image": "/gallery/image/",
        "paste": "/paste/",
        "post": "/blog/post/",
    },
)
_text2html = creoleparser.Parser(dialect, encoding=None)


def parse(txt):
    if not isinstance(txt, str):
        txt = str(txt, "utf-8")
    return _text2html(txt)

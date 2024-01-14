#!/usr/bin/python
import genshi
import creoleparser

from django.utils.html import escape

#from gallery.models import Image as GalleryImage
#from protecteddownloads.models import File as DownloadFile
#import os
#import sys

from pastebin.models import Paste
from pastebin.lib import pygmentize

def macro_paste(macro, environ, id):
    result = u""
    try:
        paste = Paste.objects.get(urlid=id)
    except Paste.DoesNotExist:
        paste = None
    if paste is not None:
        result += u'<div class="inline_paste">'
        result += u'<div class="inline_paste_head">Paste <code><a href="/paste/{id:s}/">{id:s}</a></code></div>'.format(id=id)
        result += pygmentize(paste.text, paste.lang.code)
        result += u'</div>'
    else:
        result += u'<p>Invalid paste id</p>'
    return genshi.Markup(result)

from gallery.models import Image
from sorl.thumbnail import get_thumbnail
from django.core.urlresolvers import reverse

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
    return ' '.join([ '%spx' % n for n in margin ])


def macro_image(macro, environ, id, caption=None):
    result = u""
    try:
        im = Image.objects.get(id=id)
    except Image.DoesNotExist:
        im = None
    if im is not None:
        th = get_thumbnail(im.image, "780x482")
        result += u'<div class="blogimage" style="width:{width}px;"><a href="{url}"><img style="padding:0;" src="{image}" width="{width}" height="{height}" alt="{title}" title="{title}" /></a>{caption}</div>'.format(
            margin = margin(th, 780, 482),
            image  = th.url,
            url    = reverse("gallery-image", kwargs={'id':id}),
            width  = th.x,
            height = th.y,
            title  = im.title,
            caption=caption or im.title,
        )
    else:
        result += u"<p>Invalid image id</p>"
    return genshi.Markup(result)

dialect = creoleparser.create_dialect(
    creoleparser.creole11_base,
    non_bodied_macros={
        'image'  : macro_image,
        'paste'  : macro_paste,
    },
    bodied_macros={
#        'source' : macro_pygmentize,
#        'code'   : macro_pygmentize,
#        'spoiler': macro_spoiler,
    },
    wiki_links_base_url=["/blog/post/","/gallery/image/"],
#    wiki_links_path_func=interwiki_path_test,
    interwiki_links_base_urls={
#        'wiki' : "http://wiki.urbancraft.no/wiki/", # [[wiki:SandBox|wiki test page]]  =  <a href="http://wiki.urbancraft.no/SandBox">wiki test page</a>
        'image' : "/gallery/image/",
        'paste' : "/paste/",
        'post'  : "/blog/post/",
    },

)
_text2html = creoleparser.Parser(dialect)

def parse(txt):
    if type(txt) != type(u""):
        txt = unicode(txt, "utf-8")
    return _text2html(txt)







"""
def macro_pygmentize(macro, environ, lang="text"):
    try:
        lexer = get_lexer_by_name(lang)
    except:
        lexer = get_lexer_by_name("text")
    formatter = HtmlFormatter(cssclass="source")
    result = highlight(macro.body, lexer, formatter)
    return genshi.Markup(result)

def macro_spoiler(macro, environ, title="", show=None):
    result = ""
#    result += unicode(type(show)) + u": " + unicode(show)
    result += "<div class='spoiler'>"
    if show:
        result += "<input type='button' onclick='spoilerToggle(event)' value='Hide Spoiler' class='spoiler_btn' />"
        result += "<strong>" + escape(title) + "</strong>"
        result += "<div class='spoiler_visible'>"
    else:
        result += "<input type='button' onclick='spoilerToggle(event)' value='Show Spoiler' class='spoiler_btn' />"
        result += "<strong>" + escape(title) + "</strong>"
        result += "<div class='spoiler_hide'>"
    result += parse(macro.body)
    result += "</div></div>"
    return genshi.Markup(result)
"""

"""
def macro_image(macro, environ, id, full=False):
    result = ""
    try:
        id = int(id)
        im = GalleryImage.objects.get(pk=id)
        imgurl = im.image.url
        if full:
            result += "<a href='%s'><img class='gallery_image' src='%s' title='%s' alt='%s' /></a>" %("/gallery/image/%s/" %(im.id), im.image.url, im.title, im.title)
        else:
            result += "<a href='%s'><img class='gallery_image' src='%s' title='%s' alt='%s' /></a>" %("/gallery/image/%s/" %(im.id), im.thumbnail(300, 225)['url'], im.title, im.title)

    except:
        result += "<img class='gallery_image' src='/image_error.png' alt='Image macro error' />"

    return genshi.Markup(result)
"""
"""
def macro_file(macro, environ, id, direct=False):
    result = ""
    try:
        id = int(id)
        f = DownloadFile.objects.get(pk=id)
        if direct:
            fileurl = "/downloads/file/%i/download/%s" %(id, os.path.basename(f.file.name))
 #           result += "<div class='file_download'>File: <a href='%s' title='%s'>%s</a></div>" %(fileurl, f.title, os.path.basename(f.file.name))
        else:
            fileurl = "/downloads/file/%i/" %(id)
        result += "<div class='file_download'>File: <a href='%s' title='%s'>%s</a></div>" %(fileurl, os.path.basename(f.file.name), f.title)


    except Exception, e:
        sys.stderr.write(e)
        result += "<img class='gallery_image' src='/image_error.png' alt='File macro error' />"

    return genshi.Markup(result)
"""

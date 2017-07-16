from django.http import JsonResponse
from django.shortcuts import render
from django.utils.text import slugify
from django.contrib.staticfiles.finders import get_finders
from django.contrib.staticfiles.templatetags.staticfiles import static


from posts.models import Page, Post


def manifest(request):
    j = {
        "lang": "en",
        "dir": "ltr",
        "name": request.configuration.title,
        "short_name": request.configuration.title,
        "theme_color": "#" + request.configuration.colour,
        "background_color": "#" + request.configuration.colour,
        "start_url": "/",
        "display": "standalone",
        "orientation": "natural"
    }
    return JsonResponse(j)


def service_worker(request):
    app_slug = slugify(request.configuration.title)

    urls = []
    for p in Post.objects.published():
        urls.append(p.get_absolute_url())

    for p in Page.objects.published():
        urls.append(p.get_absolute_url())

    for f in get_finders():
        for path, _ in f.list(''):
            if 'admin' not in path:
                urls.append(static(path))

    return render(request, 'sw.js', {
        'app_slug': app_slug,
        'urls': urls,
    }, content_type='application/javascript')

from .models import BlogConfiguration


def blog_configuration(request):
    return {
        'configuration': request.configuration or BlogConfiguration.get_solo()
    }


def base_url(request):
    return {
        'url': request.build_absolute_uri('/')
    }

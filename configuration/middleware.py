from .models import BlogConfiguration


def configuration_middleware(get_response):

    def middleware(request):
        request.configuration = BlogConfiguration.get_solo()
        response = get_response(request)
        return response

    return middleware

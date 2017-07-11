from .models import Page


def menu_items(request):
    return {
        'menu': Page.objects.published().filter(show_in_menu=True)
    }

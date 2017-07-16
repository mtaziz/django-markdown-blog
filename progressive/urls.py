from django.conf.urls import url

from .views import manifest, service_worker


urlpatterns = [
    url(r'^manifest.json$', manifest, name='pwa-manifest'),
    url(r'^sw.js$', service_worker, name='pwa-service-worker'),
]

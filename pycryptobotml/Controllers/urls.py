from django.http import HttpResponse, JsonResponse
from django.conf.urls import url
from .controllers import HealthController


urlpatterns = [
                url(r'^health/test', HealthController.ok),
                url(r'^health/testpost', HealthController.okpost),
            ]
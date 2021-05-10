
from django.conf.urls import include, url
from django.contrib import admin
from .Controllers import controllers

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^test/', controllers.HealthController.ok),
    url(r'^testpost', controllers.HealthController.okpost),
    # url(r'^', include('Controllers.urls')),`

]


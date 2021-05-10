from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
import logging
import json
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

class HealthController:
    @api_view(['GET'])
    def ok(request):
        okStatus= {"msg": "ok"}
        return JsonResponse(okStatus)

    @api_view(['POST'])
    def okpost(request):
        if request.method == 'POST':
            body = request.body
            loads = json.loads(request.body)

            return JsonResponse(loads)


# urlpatterns = [
#                 url(r'^health/test', HealthController.ok),
#                 url(r'^health/testpost', HealthController.okpost),
#             ]
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from metadata.functions.metadata import getConfig, configureLogging
from subscriptions.functions.subscriptions_service import getSubscriptionsService
import logging
import json
from rest_framework.decorators import api_view
from metadata.functions.service import validateCookieService

# Create your views here.

@csrf_exempt
@api_view(['GET'])
def subscriptionsView(request):
    response = {
        'data':None,
        'error':None,
        'statusCode': 1
    }
    try:
        config=getConfig()
        log=config['log']
        configureLogging(log)
        
        if 'userName' in request.COOKIES:
            if not validateCookieService(request.COOKIES['userName']):
                response['statusCode'] = 5
                raise Exception("Authentication failure")
                  
        if request.method == "GET":
            subscriptionList = getSubscriptionsService()
            response['statusCode'] = 0
            response['data'] = subscriptionList
    except Exception as e:
        logging.error(str(e))
        response['data'] = 'Error in retrieving subscription data'
        response['error'] = str(e)
    return JsonResponse(response)      
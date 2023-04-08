import json

from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from log_manager.utils.customEncoder import CustomEncoder

from log_manager import models

# Create your views here.
def queryLogs(request):
    context={}
    logs=models.Logs.objects.all()
    log_list=list()
    for log in logs:
        data = model_to_dict(log)
        log_list.append(data)
    context={'Logs':log_list}
    json_context = json.dumps(context,cls=CustomEncoder,indent=4)
    return JsonResponse(json.loads(json_context))

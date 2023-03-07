from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from sdpmanager_backend import models
from django.core import serializers



def test(request):
    context={}
    sdps=models.Sdpid.objects.all()
    sdp_list=list()
    for sdp in sdps:
        data = model_to_dict(sdp)
        sdp_list.append(data)
    context={'Sdps':sdp_list}
    print(context)
    return JsonResponse(context)
import json

from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from sdpmanager_backend import models
from django.core import serializers
import time

from sdpmanager_backend.utils.db_relate import relate_create


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


def queryComponents(request):
    context={}
    controllers=models.Controller.objects.all()
    gateways=models.Gateway.objects.all()
    sdp_list=list()
    for sdp in controllers:
        data = model_to_dict(sdp)
        data.update({'type':'controller'})
        sdp_list.append(data)
    for sdp in gateways:
        data = model_to_dict(sdp)
        data.update({'type': 'gateway'})
        sdp_list.append(data)
    context={'Sdps':sdp_list}
    print(context)
    return JsonResponse(context)


def RegSdp(request):
    form = request.POST
    time_stamp=time.time()
    time_array = time.localtime(time_stamp)
    other_way_time = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
    sdp=models.Sdpid.objects.create(
        country= form.get('country'),
        state= form.get('state'),
        locality= form.get('locality'),
        org= form.get('org'),
        org_unit= form.get('org_unit'),
        alt_name= form.get('alt_name'),
        email= form.get('email'),
        type= form.get('type'),
        valid= form.get('valid'),
        last_cred_update= other_way_time,
        cred_update_due= other_way_time,
        serial= form.get('serial')
    )
    ret=relate_create(sdp,form)
    print(ret)
    return HttpResponse('received')
def DelSdp(request):
    command=request.body
    json_param = json.loads(command.decode())
    sdpid=json_param.get('Delsdpid')
    print(sdpid)
    ret=None
    sdp=models.Sdpid.objects.get(sdpid=sdpid)
    if sdp:
        ret=sdp.delete()
        print(ret)
    return HttpResponse(ret)

def EditSdp(request):
    form = request.POST
    print(form)
    time_stamp=time.time()
    time_array = time.localtime(time_stamp)
    other_way_time = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
    sdp=models.Sdpid.objects.get(sdpid=form.get('sdpid'))
    sdp.country= form.get('country')
    sdp.state= form.get('state')
    sdp.locality= form.get('locality')
    sdp.org= form.get('org')
    sdp.org_unit= form.get('org_unit')
    sdp.alt_name= form.get('alt_name')
    sdp.email= form.get('email')
    sdp.type= form.get('type')
    sdp.valid= form.get('valid')
    sdp.last_cred_update= other_way_time
    sdp.cred_update_due= other_way_time
    sdp.serial= form.get('serial')
    ret=sdp.save()
    print(ret)
    return HttpResponse('received')
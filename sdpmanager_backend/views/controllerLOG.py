import json

from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from sdpmanager_backend import models
from django.core import serializers
import time


def LogConnection(request):

    logs = request.body
    print(logs)
    return HttpResponse("received")
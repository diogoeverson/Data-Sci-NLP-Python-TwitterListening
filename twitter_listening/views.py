from django.core import serializers
from django.forms import model_to_dict
from django.shortcuts import render
from bson import json_util
from .models import tweets
import json


def index(request):
    model_to_dict(tweets)
    return render(request, 'index.html', tweets)

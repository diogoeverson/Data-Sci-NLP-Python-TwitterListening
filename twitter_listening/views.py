from django.core import serializers
from django.shortcuts import render
from bson import json_util
from .models import tweets
import json


def index(request):
    results = tweets.vali_collection.find({'index': []})
    json_docs = [json.dumps(doc, default=json_util.default) for doc in results]
    return render(request, 'index.html', {'results': json_docs[0:3]})

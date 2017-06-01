# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from django.template import loader
import requests
import json

# Create your views here.

def index(request):
    return HttpResponse('Hello World!')

def profile(request):
    parsedData = []
    if request.method == 'POST':
        print request.POST
        keyword = request.POST.get('keyword')
        #keyword = "python"
        req = requests.get('https://jobs.github.com/positions.json?description=' + keyword + '&location=san+francisco')
        jsonList = []
        jsonList.append(json.loads(req.content))
        for job in jsonList:
            for data in job:
                jobData = {}
                jobData['title'] = data['title']
                jobData['company'] = data['company']
                jobData['company_logo'] = data['company_logo']
                parsedData.append(jobData)

    return render(request, 'gitsearchapp/profile.html', {'data': parsedData})

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from django.template import loader
import requests
import json

# Create your views here.

def index(request):
    parsedData = []
    if request.method == 'POST':
        print request.POST
        keyword = request.POST.get('keyword')
        req = requests.get('https://jobs.github.com/positions.json?description=' + keyword + '&location=san+francisco')
        jsonList = []
        jsonList.append(json.loads(req.content))
        for job in jsonList:
            for data in job:
                jobData = {}
                jobData['title'] = data['title']
                jobData['company'] = data['company']
                jobData['company_logo'] = data['company_logo']
                jobData['id'] = data['id']
                parsedData.append(jobData)

    return render(request, 'gitsearchapp/profile.html', {'data': parsedData})

def detail(request):
    job_id = request.GET.get('id')
    req = requests.get('https://jobs.github.com/positions/' + job_id + '.json')
    return HttpResponse(req)
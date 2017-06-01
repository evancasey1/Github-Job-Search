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

    return render(request, 'gitsearchapp/index.html', {'data': parsedData})

def detail(request):
    parsedData = []
    job_id = request.GET.get('id')
    req = requests.get('https://jobs.github.com/positions/' + job_id + '.json?markdown=true')

    jsonList = []
    jsonList.append(json.loads(req.content))
    jobData = {}
    for data in jsonList:
        jobData['title'] = data['title']
        jobData['company'] = data['company']
        jobData['description'] = data['description']
        jobData['company_url'] = data['company_url']

    parsedData.append(jobData)
    return render(request, 'gitsearchapp/detail.html', {'data': parsedData})
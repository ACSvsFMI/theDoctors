from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views.generic import View
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.tools import run
from oauth2client.file import Storage
from django.http import HttpResponse
import apiclient.discovery
import httplib2
import pprint
import os.path
import time
import urllib
import json

class SuggestionView(View):
    
    def get(self, request, *args, **kwargs):
        #if request.user.is_authenticated() is False:
        #   return redirect('/login')
        api_key = 'AIzaSyAAPuaXCEEUGGZe27ezqxP3sM4YvbRd5n0'

        if 'name' in request.GET:
            http = httplib2.Http()
            service = apiclient.discovery.build('plus', 'v1', http=http, developerKey=api_key)
            persons = service.people().search(maxResults=10, query=request.GET['name']).execute()
            if 'items' in persons:
                return HttpResponse(json.dumps(persons['items']), mimetype="application/json")
        return HttpResponse('[]', mimetype="application/json")

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def m_admin_test(request):
    if request.method == 'POST':
    	data = {'foo': 'bar', 'hello': 'world'}
    	return HttpResponse(json.dumps(data), content_type='application/json')
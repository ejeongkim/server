from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def m_admin_test(request):

    adminList = ["hi","admin1@com", "admin2@com", "admin3@com", "admin4@com", "admin5@com", "admin6@com", "admin7@com", "admin8@com", "admin9@com", "admin10@com", "admin11@com", "admin12@com", "admin13@com"]

    if request.method == 'POST':
    	data = {'foo': 'bar', 'hello': 'world'}
    	return HttpResponse(json.dumps(data), content_type='application/json')
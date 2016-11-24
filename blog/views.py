from django.shortcuts import render
from django.http import HttpResponseRedirect
#, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
# Create your views here.
@csrf_exempt
def m_admin_test(request):
	adminList = ["hi","admin1@com", "admin2@com", "admin3@com", "admin4@com", "admin5@com", "admin6@com", "admin7@com", "admin8@com", "admin9@com", "admin10@com", "admin11@com", "admin12@com", "admin13@com"]
    if request.method == 'POST':
		data = {'foo': 'bar', 'hello': 'world', 'ejeong': 'ejeongkim1!'}
		return JsonResponse({"employees":[
			{"firstName":"John", "lastName":"Doe"},
			{"firstName":"Anna", "lastName":"Smith"},
			{"firstName":"Peter", "lastName":"Jones"}]})
		#return HttpResponse(json.dumps(data), content_type='application/json')
		# msg_  = request.POST['msg']
		# if adminList.__contains__(msg_):
		# 	return HttpResponse('success')
		# else:
		# 	return HttpResponse('fail')
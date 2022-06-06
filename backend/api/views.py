#from django.shortcuts import render

# Create your views here.

import json
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product

# # defining a function based view
# def api_home(request, *args, **kwargs):
#     # # request is an instance of HttpRequest class
#     # # request.body => accepts that json data that can be echoed.
#     # body = request.body # byte string of JSON data OR stringified version of a JSON object
#     # data = {}
#     # try: 
#     #     data = json.loads(body) # converts byte string of JSON data -> to -> Python Dict
#     # except:
#     #     pass

#     # print(data)

#     # data['params'] = request.GET #gives all query parameters
#     # data['headers'] = dict(request.headers)
#     # data['content_type'] = request.content_type

#     modelData = Product.objects.all().order_by("?").first()
#     data = {}
#     if modelData:
#         # data['id'] = modelData.id
#         # data['title'] = modelData.title
#         # data['content'] = modelData.content
#         # data['price'] = modelData.price
#         data = model_to_dict(modelData,  fields=['id', 'title', 'price'])
#         #jsonDataString = json.dumps(data)

#     return JsonResponse(data)
#     #return HttpResponse(jsonDataString, headers={"content-type": "application/json"})

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    modelData = Product.objects.all().order_by("?").first()
    data = {}
    if modelData:
        data = model_to_dict(modelData, fields = ['id', 'title', 'price'])
    
    return Response(data)
#from django.shortcuts import render

# Create your views here.

import json
from django.http import JsonResponse


# defining a function based view
def api_home(request, *args, **kwargs):
    # request is an instance of HttpRequest class

    # request.body => accepts that json data that can be echoed.
    body = request.body # byte string of JSON data OR stringified version of a JSON object
    data = {}
    try: 
        data = json.loads(body) # converts byte string of JSON data -> to -> Python Dict
    except:
        pass

    print(data)

    data['params'] = request.GET #gives all query parameters
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type

    return JsonResponse(data)
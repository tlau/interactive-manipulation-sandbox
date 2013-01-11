from django.http import HttpResponse
import json

def client(request):
    response_obj = make_user_json( request.user)
    return HttpResponse(json.dumps(response_obj))

def make_user_json( user):
    if user.username == '':
        return {
            'username': 'AnonymousUser',
            'first_name': '',
            'last_name': 'Anonymous'
        }
    else:
        return {
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name
        }

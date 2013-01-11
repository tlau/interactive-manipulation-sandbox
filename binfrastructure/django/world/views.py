from django.http import HttpResponse
from django.shortcuts import *
from django.contrib.auth.decorators import login_required
from world.models import *
from django.contrib.auth.models import User, AnonymousUser
import json
import datetime
from django.utils.timezone import utc
from django.conf import settings

# Create your views here.

def index(request):
    return render_to_response('index.html', {'user': request.user})

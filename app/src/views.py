from django.core import serializers
from django.shortcuts import render
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .forms import RegisterForm
from .models import Users


def index(request):
    return render(request, 'index.html', {'users': Users.objects.all()})


@require_http_methods('POST')
@csrf_exempt
# just sample app so ignore csrf
def register(request):
    print(request.POST)
    if request.POST.get('client') != 'app':
        print("WEBBB")
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            user.refresh_from_db()

            user.username = form.cleaned_data.get('username')
            user.email = form.cleaned_data.get('email')
            user.birthday = form.cleaned_data.get('birthday')
            user.address = form.cleaned_data.get('address')
            user.save()

            data = {
                'result': True,
                'message': 'User is recorded with given informations.'
            }
            return HttpResponse(json.dumps(data), content_type='application/json', status=201)
        else:
            data = {
                'result': False,
                'message': form.errors
            }
            return HttpResponse(json.dumps(data), content_type='application/json', status=202)
    else:
        print("APPPP")
        try:
            username = request.POST.get('username')
            email = request.POST.get('email')
            birthday = request.POST.get('birthday')
            address = request.POST.get('address')

            if not all([username, email, birthday, address]):
                raise Exception("All fields should be entered!")

            if Users.objects.filter(username=username).exists():
                raise Exception("Member already recorded!")

            # record the user with given information
            user = Users(username=username, email=email, birthday=birthday, address=address)
            Users.save(user)

            data = {
                'result': True,
                'message': 'User is recorded with given informations.'
            }
            return HttpResponse(json.dumps(data), content_type='application/json', status=201)
        except Exception as e:
            data = {
                'result': False,
                'message': str(e)
            }
            return HttpResponse(json.dumps(data), content_type='application/json', status=202)


@require_http_methods('GET')
def users(request):
    users_json = serializers.serialize('json', Users.objects.all())
    return HttpResponse(users_json, content_type='application/json')


@require_http_methods('GET')
def user(request):
    username = request.GET.get("username")
    u = {}
    if Users.objects.filter(username=username).exists():
        user_object = Users.objects.filter(username=username)
        u = json.loads(serializers.serialize("json", user_object))[0]

    return HttpResponse(json.dumps(u), content_type="application/json")


@require_http_methods('GET')
def ping(request):
    return HttpResponse("pong", content_type='text', status=200)

from django.core import serializers
from django.shortcuts import render
from src.forms import RegisterForm
import json
from django.http import HttpResponse
from src.models import Users
from django.views.decorators.csrf import csrf_exempt


def index(request):
    users = Users.objects.all()

    return render(request, 'index.html', {'users': users})

@csrf_exempt
def register(request):
    if request.method == 'POST':
        if request.POST.get('client') != 'app':
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

    else:
        form = RegisterForm()

    users = Users.objects.all()
    return render(request, 'index.html', {'users': users})


def users(request):
    if request.method == "GET":
        users = Users.objects.all()
        users_json = serializers.serialize('json', users)

        return HttpResponse(users_json, content_type='application/json')

from django.shortcuts import render, HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt




def sign_in_view(request):
    print("login page")
    template = loader.get_template('user/signup.html')
    return HttpResponse(template.render())


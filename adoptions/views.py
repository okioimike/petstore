from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<p><h3>This is the Home View</h3></p>')

def pet_detail(request,pet_id):
    return HttpResponse(f'<p>Pet detail view with {pet_id} as id</p>')

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.http.request import HttpRequest


def index(request: HttpRequest) -> HttpResponse:
	data = {
	}
	return render(request, 'index.html', data)

# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, HttpResponse
def index(request):
        return render(request,'cam/index.html')

# Create your views here.

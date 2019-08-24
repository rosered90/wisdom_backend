# _*_ coding:utf-8 _*_
from django.shortcuts import render


def receive_gps(request):
    return render(request, 'index.html', locals())
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def homeTest(request):
    return render(request, "home.html")

def postTest(request):
    return render(request, "posts/posts_test.html")
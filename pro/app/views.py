from django.shortcuts import render

# Create your views here.



from django.http import HttpResponse


# def home(request):
#
#     if(request.method=="GET"):
#         return HttpResponse("Welcome to Django")
#
# #index views return message  "index page"
#
#
# def Index(request):
#     if(request.method=="GET"):
#         return HttpResponse("Index pages")

from django.views import view


class Home(view):
    def get(self,request):
        return HttpResponse("welcome to Django")


class Index(view):
    def get(self,request):
        return HttpResponse("Index")


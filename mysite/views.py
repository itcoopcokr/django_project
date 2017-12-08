from django.views.generic import View
from django.shortcuts import render

class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request,"home.html", { } )

class Base(View):
    def get(self, request, *args, **kwargs):
        return render(request,"base.html", { } )

class Team(View):
    def get(self, request, *args, **kwargs):
        return render(request,"team.html", { } )
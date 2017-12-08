from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render

class Team(View):
    def get(self, request, *args, **kwargs):
        context = {
            "name":"john"
        }
        return render(request,"team.html", context )
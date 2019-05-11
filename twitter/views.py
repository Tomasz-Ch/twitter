from django.shortcuts import render
from django import views


class MainWebpageView(views.View):
    def get(self, request):
        ctx = {}
        return render(request, 'twitter/index.html', ctx)

from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # On définit une date à partir de datetime.today
    return render(request, "DocBlog/index.html", context={"date": datetime.today()})
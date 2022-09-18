from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def info(request):
    return render(request, "info.html")

def login(request):
    return render(request, "login.html")

def table(request):
    return render(request, "table.html")

def image(request):
    return render(request, "image.html")

def examples(request):
    return render(request, "examples.html")

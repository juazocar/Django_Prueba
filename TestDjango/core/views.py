from django.shortcuts import render


# Create your views here.

def home(request):
    contexto = {"nombre":"Claudia Andrea"}
    return render(request, 'core/home.html', contexto)
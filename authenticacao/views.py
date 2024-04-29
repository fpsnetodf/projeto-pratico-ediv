from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .forms import RegisterForm

# Create your views here.


def register(request: HttpResponse) -> HttpResponse:
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'authenticacao/register.html', {"form":form})
    
    elif request.method == 'POST':
        return HttpResponse("Você esta submetendo esse formulario!!")
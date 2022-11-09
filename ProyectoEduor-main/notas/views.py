from django.shortcuts import render,redirect

# Create your views here.

def notas(request):
    return render(request,'notas.html')

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

    
def contactenos(request):
    return render(request, 'contactenos.html');
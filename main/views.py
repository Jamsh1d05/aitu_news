from django.shortcuts import render

def indexHandler(request):
    return render(request, 'index.html')
from django.shortcuts import render

def lab_home(request):
    return render(request, 'lab/lab_home.html')
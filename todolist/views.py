from django.shortcuts import render

def base(request):
    return render(request, 'todolist/base.html')

def about(request):
    return render(request, 'todolist/about.html')

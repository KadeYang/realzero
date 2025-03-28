from django.shortcuts import render

def index(request):
    return render(request, 'homepage/index.html')

def ranking(request):
    return render(request, 'homepage/ranking.html')

def community(request):
    return render(request, 'homepage/community.html')

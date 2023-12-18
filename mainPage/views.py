from django.shortcuts import render

def index(request):
    return render(request, 'mainPage/homePage.html')

def contacs(request):
    return render(request, 'mainPage/basic.html', {'values': ['Github:', 'vadim-proger']})
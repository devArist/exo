from django.shortcuts import render


def index(request):
    
    return render(request,'index.html')


def about(request):
    
    return render(request,'about.html')


def contact(request):
    
    return render(request,'contact.html')

def shop(request):
    
    return render(request,'shop.html')

def shop_single(request):
    
    return render(request,'shop-single.html')
# Create your views here.

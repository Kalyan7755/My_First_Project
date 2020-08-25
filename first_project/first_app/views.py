from django.shortcuts import render

def home(request):
    return render(request,'home.html')
def add(request):
    a = request.POST.get('a')
    b = request.POST.get('b')
    c = int(a) + int(b)
    return render(request,'add.html',{'c' : c})


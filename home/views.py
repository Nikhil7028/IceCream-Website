from django.shortcuts import render, HttpResponse # type: ignore

# Create your views here.
def index(request):
    context={
        'variable1': 'This is the value of varible1',
        'variable2': 'Nikhil is great person '
    }
    return render(request,'index.html')
    # return HttpResponse("Hello, world!")
def home(request):
    return render(request,'index.html')
def service(request):
    return render(request,'services.html')
def contact(request):
    return render(request,'contact.html')
def more(request):
    return render(request,'more.html')
def aboutus(request):
    return render(request,'aboutus.html')

from django.shortcuts import render, HttpResponse # type: ignore
from datetime import datetime
from home.models import Contact
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
def more(request):
    return render(request,'more.html')
def aboutus(request):
    return render(request,'aboutus.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name= name, email=email, phone= phone, desc= desc, date= datetime.today())
        contact.save()
    return render(request,'contact.html')

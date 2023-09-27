from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from datetime import datetime
from home.models import Contact
from home.models import Apply


# Create your views here.
def index(request):
    return render(request,'index.html')
    # return HttpResponse("This is the home page")  

def about(request):
    # return HttpResponse("This is the about page")  
    return render(request,'about.html')
    

def career(request):
    # return HttpResponse("This is the services page")  
    return render(request,'career.html')


def contact(request):
    context = {'success': False}
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name = name, email = email, phone = phone, message = message, date = datetime.today())
        contact.save()
        context = {'success': True}
    return render(request,'contact.html',context)

def apply(request):
    # return HttpResponseRedirect("apply.html") 
    context = {'success': False} 
    if request.method == "POST":
        Name = request.POST.get('Name')
        Email = request.POST.get('Email')
        Phone = request.POST.get('Phone')
        # address = request.POST.get('address')
        
        resume = request.POST.get('resume')
        # Message = request.POST.get('Message')
        apply = Apply(Name = Name, Email = Email, Phone = Phone, resume = resume , date = datetime.today())
        apply.save()
    return render(request,'apply.html',context)
            ### job apply ma click mate 
            
def require(request):
    # return HttpResponse("This is the services page")  
    return render(request,'require.html')
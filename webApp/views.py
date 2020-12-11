from django.shortcuts import render
from .models import Contact

# Create your views here.
def home(request):
    return render(request,'index.html')

def contact(request):
    if request.method == "GET":
        return render(request,'contact.html')
    if request.method == "POST":
        c_name = request.POST.get("name")
        c_email = request.POST.get("email")
        c_subject = request.POST.get("subject")
        c_message = request.POST.get("message")
        sql = Contact(name=c_name,email=c_email,subject=c_subject,message=c_message)
        sql.save()
        sucess = {
            "message":"ok"
        }
        return render(request,'contact.html',context=sucess)

def portfolio(request):
    return render(request,'portfolio.html')

def services(request):
    return render(request,'services.html')
def pricing(request):
    return render(request,'pricing.html')

def blog(request):
    return render(request,'blog.html')
    
def blog_single(request):
    if request.method == "GET":
        return render(request,'blog-single.html')
    
def about(request):
    return render(request,'about.html')

def team(request):
    return render(request,'team.html')
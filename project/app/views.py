from django.shortcuts import render
from app import models
from .models import Contact


# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        obj = Contact(name=name, email=email, subject=subject, message=message)
        obj.save()
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def resume(request):
    return render(request, 'resume.html')


# def contact(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         subject = request.POST['subject']
#         message = request.POST['message']
#         print(name, email, subject, message)
#         obj=Contact( name='name',email='email',subject='subject', message='message' )
#         obj.save()
#     return render(request, 'contact.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        obj = Contact(name=name, email=email, subject=subject, message=message)
        obj.save()
    return render(request, 'contact.html')

from django.shortcuts import render
from .models import contactData
from django.http import HttpResponse

def contactdata(request):
    if request.method =='GET':
        return render(request,'contactdata.html')
    else:
        contactData(
        first_name=request.POST['fname'],
        last_name=request.POST['lname'],
        email=request.POST['email'],
        mobile=request.POST['mobile'],
        course=request.POST['course'],
        location=request.POST['location']
        ).save()
        return render(request,'contactdata.html')

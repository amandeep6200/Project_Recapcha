import json
import requests
import urllib
import urllib3
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

def index(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        print(email,password)


        clientkey = 'g-recaptcha-response'
        secretkey = '6Lci2esUAAAAAKf5Hr5g57rQe1mP5jVeJ9Ilu4YP'
        captchadata = {
            'secret': secretkey,
            'response': clientkey
        }

        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=captchadata)

        #response=r.json()
        response=json.loads(r.text)
        verify=response['success']
        print("success is verify:",verify)
        if verify:
            return render(request,'index1.html')
        else:
            return render(request,'index2.html')



    return render(request,'index.html')
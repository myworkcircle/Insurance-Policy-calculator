from django.shortcuts import render,redirect
# from .form import excel
from django import http
from django.http import HttpResponse
from .models import file
from django import forms
import datetime
import pyrebase
from django.contrib import auth
from firebase import firebase
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.core.paginator import Paginator as pg
from django.views.generic import View
from .render import Render
from django.utils import timezone



config = {
  "apiKey": "AIzaSyBRhcglITIITfWvzBUuHcw6yoetAGaiKRg",
  "authDomain": "euclid-master.firebaseapp.com",
  "databaseURL": "https://euclid-master.firebaseio.com",
  "storageBucket": "euclid-master.appspot.com"
}

firebase = pyrebase.initialize_app(config)
#firebase = firebase.FirebaseApplication('https://euclid-master.firebaseio.com')
db = firebase.database()

def fir(request):
    number = db.child('PrimiumTable').get().val()
    number = list(number)
    counter = []
    for i in range(0,len(number)):
      counter.append(i)
    print(number)
    premium=[]
    product = []
    tenure = []
    for i in range(0,len(number)):
      premi = db.child("Primium Table").child(i).child('ppremium').get().val()
      prod = db.child('Primium Table').child(i).child('ptittle').get().val()
      ten = db.child('Primium Table').child(i).child('ptenure').get().val()
      tenure.append(ten)
      premium.append(premi)
      product.append(prod)
     
    paginator = pg(premium,5)
    page = request.GET.get('page')
    num = paginator.get_page(page)  
    final = zip(premium,product,tenure,counter)
    
    # return render(request,"temp/Premium Table.html",{'premium':premium,'product':product})
    return render(request,"temp/policy.html",{'final':final,'premium':num})

def view(request,id):
    # doc = file.objects.all()
    print(id)
    # number = db.child("New Sales").get().val()
    # number = list(number)
    
    name = db.child("New Sales").child(id).child('name').get().val()
    dob = db.child('New Sales').child(id).child('dob').get().val()
    contact = db.child('New Sales').child(id).child('contact').get().val()
    address = db.child('New Sales').child(id).child('address').get().val()
    customer = db.child('New Sales').child(id).child('customer_id').get().val()
    marital = db.child('New Sales').child(id).child('marital_status').get().val()
    age = db.child('New Sales').child(id).child('age').get().val()
    gender = db.child('New Sales').child(id).child('gender').get().val()
    fh = db.child('New Sales').child(id).child('father_husband_name').get().val()
      
    return render(request,"temp/view.html",{
      'name':name,
      'dob':dob,
      'contact':contact,
      'address':address,
      'customer':customer,
      'marital':marital,
      'gender':gender,
      'age':age,
      'fh_name':fh,
      # 'doc': doc[4]
      })    

# def dummy_input(request):
#     form = excel(request.POST)
#     if form.is_valid():
#         form.save() 
#         return redirect('/kantap') 
#     form = excel()    
#     context={
#         'form':form
#     }
#     return render(request, "dummy/data_input.html",context)

def police(request):
    return render(request,"temp/policy.html")

def index(request):
    return render(request,"temp/index.html")

class Pdf(View):


    def get(self, request):

      doc = file.objects.all()
      number = db.child("New Sales").get().val()
      number = list(number)
      address=[]
      age = []
      contact = []
      customer = []
      gender = []
      marital = []
      status = []
      dob = []
      name = []
      fh = []
      for i in range (0,len(number)):
        nam = db.child("New Sales").child(i).child('name').get().val()
        do = db.child('New Sales').child(i).child('dob').get().val()
        cont = db.child('New Sales').child(i).child('contact').get().val()
        addr = db.child('New Sales').child(i).child('address').get().val()
        cust = db.child('New Sales').child(i).child('customer_id').get().val()
        marit = db.child('New Sales').child(i).child('marital_status').get().val()
        ag = db.child('New Sales').child(i).child('age').get().val()
        gend = db.child('New Sales').child(i).child('gender').get().val()
        fh_name = db.child('New Sales').child(i).child('father_husband_name').get().val()
        name.append(nam)
        dob.append(do)
        contact.append(cont)
        address.append(addr)
        customer.append(cust)
        marital.append(marit)
        age.append(ag)
        gender.append(gend)
        fh.append(fh_name)

      return Render.render("temp/view.html",{
        'name':name,
        'dob':dob,
        'contact':contact,
        'address':address,
        'customer':customer,
        'marital':marital,
        'gender':gender,
        'age':age,
        'fh_name':fh,
        'doc': doc,
        'premium': premium
        })    
        # return Render.render('invoice.html', params)




# name = firebase.get('Premium Table',None)
    # a = list(name)
    # number = []
    # for i in a:
    #   prem = firebase.get('Premium Table/'+i,'Premium')
    #   number.append(prem)
    # 
    # premium = firebase.get('Premium Table/'+a,'Premium')
    # product = firebase.get('Premium Table/'+a,'Product')
    
    # newsales = firebase.get('New Sales',None)
    # b = list(newsales)

    # premium = str(premium)
    # print(premium)
    # return render(request,"temp/Premium Table.html",{'premium':premium,'product':product})




    # name.append(nam)
    #   dob.append(do)
    #   contact.append(cont)
    #   address.append(addr)
    #   customer.append(cust)
    #   marital.append(marit)
    #   age.append(ag)
    #   gender.append(gend)
    #   fh.append(fh_name)

    # address=[]
    # age = []
    # contact = []
    # customer = []
    # gender = []
    # marital = []
    # status = []
    # dob = []
    # name = []
    # fh = []
    # for i in rangelen(number)):
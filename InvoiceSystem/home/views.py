from django.shortcuts import render,HttpResponse,redirect
from home .models import Customers
from home.filters import *
import json

# Create your views here.
# admin is vaibhav  1234

def index(request):
    return render(request,'index.html')



def invoice(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        items=request.POST.get('itemsval')
        price=request.POST.get('pricesval')
        quantity=request.POST.get('quantitiesval')
        # print(items)
        # print(price)
        # print(quantity)

        userdetail=Customers(name=name,email=email,phone=phone,address=address,quantities=quantity,prices=price,itempurchase=items)
        # print("USERDETAIL:",userdetail)
        # return HttpResponse("hello")
        userdetail.save()
    return redirect('alluser_detail')

def alluser_detail(request):
    customers=Customers.objects.all()
    myfilter=CustomerFilter(request.GET,queryset=customers)
    customers=myfilter.qs
    print(customers)
    

    context={'customers':customers,'customers':customers,'myfilter':myfilter}

    return render(request,'alluser.html',context)


def userdetails(request,pk):
    customer=Customers.objects.get(id=pk)
    print(pk)
    print(type(pk))
    items=json.loads(customer.itempurchase)
    prices=json.loads(customer.prices)
    quantity=json.loads(customer.quantities)
    result=[]
    totalamount=0
    print(type(items))
    print(type(prices))
    print(type(quantity))
    
    
    for i in range(len(items)):
        
        result.append({"items":items[i],"prices":prices[i],"quantity":quantity[i],"totalamount":prices[i]*quantity[i]})
        totalamount=totalamount+(prices[i]*quantity[i])


    context={"custom":result,"totalamount":totalamount,"customer":customer}

    return render(request,'userdetail.html',context)


def newbill(request):
    return render(request,'index.html')
    
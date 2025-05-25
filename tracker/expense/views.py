from django.shortcuts import render,redirect
from expense.models import TrackingHistory,CurrentBalance
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login


def login_view(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password = request.POST.get('password')
        
        user = User.objects.filter(username = username)
        if not user.exists():
            messages.success(request , 'Account Not Found')
            return redirect('/login/')
        
        user = authenticate(username=username,password=password)
        if not user:
            messages.success(request , 'Incorret password')
            return redirect('/login/')  
        login(request,user)
        return redirect("/")
    
            
            
            
    return render(request,"login.html")

def register_view(request):
       if request.method == 'POST':
          username = request.POST.get('username')
          password = request.POST.get('password')
          first_name = request.POST.get('first_name')
          last_name = request.POST.get('last_name')
       
          user = User.objects.filter(username=username)
          if user.exists():
             messages.success(request , 'Username is already taken')
             return redirect('/register/')
    
          user = User.objects.create(
                 username=username,
                 first_name=first_name,
                 last_name=last_name
                )
    # if we write the password inside the create , then our password is not encrypted 
          user.set_password(password) 
          user.save()
          messages.success(request, ' Account created sucessfully')
          return redirect('/register/')


       return render(request,'register.html')


def index(request):
    if request.method=='POST':
       amount=request.POST.get('amount')
       description=request.POST.get('description')
       current_balance,_ = CurrentBalance.objects.get_or_create(id=1)
       expence_type = 'CREDIT'
       if float(amount) < 0:
           expence_type ='DEBIT'
        
       tracking_history=TrackingHistory.objects.create(
          amount=amount,
          current_balance=current_balance,
          description=description,
          expence_type = expence_type,
         
       )
       current_balance.current_balance += float(tracking_history.amount)
       current_balance.save()
       return redirect('/')
    current_balance,_ = CurrentBalance.objects.get_or_create(id=1)
    income = 0
    expence =0
    for tracking_history in TrackingHistory.objects.all():
        if tracking_history.expence_type == 'CREDIT':
           income = tracking_history.amount
        else :
           expence = tracking_history.amount
    context = {'income':income,'expence':expence,'transactions': TrackingHistory.objects.all(),'current_balance': current_balance}
    return render(request, 'index.html', context)
 

def delete_transaction(request,id):
    tracking_history = TrackingHistory.objects.filter(id=id)
    
    if tracking_history.exists():
        current_balance,_ = CurrentBalance.objects.get_or_create(id=1)
        tracking_history =  tracking_history[0]
        
        current_balance.current_balance = current_balance.current_balance - tracking_history.amount
        current_balance.save()
        
    tracking_history.delete()
    return redirect('/')
    
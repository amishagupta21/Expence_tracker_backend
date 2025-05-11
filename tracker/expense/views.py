from django.shortcuts import render,redirect
from expense.models import TrackingHistory,CurrentBalance


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
    return render(request,'index.html')
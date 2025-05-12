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
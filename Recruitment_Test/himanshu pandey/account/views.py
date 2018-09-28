from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import bankaccount


def index(request):
    all_accounts= bankaccount.objects.all()
    context = { 'all_accounts': all_accounts}
    return render(request, 'account/index.html', context)

def detail(request, bankaccount_id):
    try:
        bankaccounts = bankaccount.objects.get(pk=bankaccount_id)
    except bankaccount.DoesNotExist:
        raise Http404("The account does not exist")
    return render(request, 'account/detail.html', {'bankaccount': bankaccounts})

def calc(request,Bankaccount_balance):
    try:
        Bankaccount=bankaccount.objects.get(balance=Bankaccount_balance)
    except bankaccount.DoesNotExist:
        raise Http404("Account does not exist")
    if int(Bankaccount_balance)<10000:
        total=int(Bankaccount_balance)*0.10
        net_balance=int(Bankaccount_balance)-total
        return HttpResponse("<marquee>Tax slab 10 percent and tax payable is:"+str(total)+"<br> Final balance is:"+str(net_balance)+"</marquee>")
    elif int(Bankaccount_balance)<20000 and int(Bankaccount_balance)>10000:
        total=int(Bankaccount_balance)*0.15
        net_balance=int(Bankaccount_balance)-total
        return HttpResponse("<marquee>Tax slab 15 percent and tax payable is:"+str(total)+" <br>Final balance is:"+str(net_balance)+"</marquee>")
    else:
        total = int(Bankaccount_balance) * 0.20
        net_balance = int(Bankaccount_balance)- total
        return HttpResponse("<marquee>Tax slab 20 percent and tax payable is:" + str(total)+"<br> Final balance is:"+str(net_balance)+ "</marquee>")



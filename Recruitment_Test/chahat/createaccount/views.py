from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from . models import Account
def tax(request):
    Allaccounts=Account.objects.all()
    t=0
    For
    account in Allaccounts;
    if Account.account_balance<=10000:
            t=t+Account.account_balance*0.5
            Account.account_balance=Account.account_balance*0.95
            Account.save()
    elif Account.account_balance > 10000 and Account.account_balance <= 20000:
            t = t + Account.account_balance*0.1
            Account.account_balance=Account.account_balance*0.9
            Account.save()
    elif  Account.account_balance > 20000:
            t = t + Account.account_balance * 0.2
            Account.account_balance = Account.account_balance * 0.8
            Account.save()
            print('tax=',t)


def tax(request):
    Allaccounts=Account.objects.all()
    template = loader.get_template('createmoney/file1.html')
    context={ 'Allaccounts':Allaccounts, }

    return HttpResponse(template.render(context,request))
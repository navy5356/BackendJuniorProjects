from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Account
from django.template import loader


def show(request):
    all_account = Account.objects.all()
    # all_account = Account.objects.exclude(Name="RevenueAccount")
    template = loader.get_template('revenue/index.html')
    context = {
        'all_account': all_account
    }
    return HttpResponse(template.render(context, request))

def collect(request):
    all_account = Account.objects.exclude(Name="RevenueAccount")
    revenue = 0
    for account in all_account:
        if account.Amount <= 10000:
            revenue = revenue + round(float(account.Amount)*0.05,2)
            account.Amount = round(float(account.Amount)*0.95,2)
            account.save()
        elif account.Amount <= 20000:
            revenue = revenue + round(float(account.Amount)*0.10,2)
            account.Amount = round(float(account.Amount)*0.90,2)
            account.save()
        else:
            revenue = revenue+round(float(account.Amount)*0.15,2)
            account.Amount = round(float(account.Amount)*0.85,2)
            account.save()
    raccount = Account.objects.filter(Name="RevenueAccount").first()
    raccount.Amount = round(float(raccount.Amount),2) + revenue
    raccount.save()
    return HttpResponseRedirect('/revenue/')

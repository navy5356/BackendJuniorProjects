# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Accounts
from django.shortcuts import render
from decimal import *


# Home page
def home(request):
    all_accounts = Accounts.objects.all()
    context = {
        'all_accounts' : all_accounts
    }
    return render(request, 'account/home.html', context)


# On-Click Account details
def detail(request, account_id):
    acc = Accounts.objects.get(pk=account_id)
    return render(request, 'account/AccDetails.html', {'acc': acc})


# Accessing the tax page
def taxman(request):
    all_accounts = Accounts.objects.all()
    return render(request, 'account/taxman.html', {'all_accounts': all_accounts})


# Tax deduction
def deduct(request):
    all_accounts= Accounts.objects.all()
    tax_acc = Accounts.objects.get(name='Revenue Department')
    slab = 0
    for user_acc in all_accounts:
        if(user_acc.name!='Revenue Department'):
            if (user_acc.balance >0) and (user_acc.balance < 10000):
                slab = 0.05
                # print(slab)
            elif(user_acc.balance > 10000 ) and (user_acc.balance<20000):
                slab = 0.10
                # print(slab)
            elif(user_acc.balance >20000):
                slab = 0.15
                # print(slab)
            tax = user_acc.balance * Decimal(slab)
            user_acc.balance -= Decimal(tax)
            tax_acc.balance += Decimal(tax)
            user_acc.save()
            tax_acc.save()
    return render(request, 'account/deducted.html', {})


# Adding a new account
def post(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('balance'):
            acc = Accounts()
            acc.name = request.POST.get('name')
            acc.balance = request.POST.get('balance')
            acc.save()
            return render(request, 'account/post.html', {})
    else:
        return render(request, 'account/post.html', {})


# Depositing Money
def dep(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('amount'):
            u_name = request.POST.get('name')
            acc = Accounts.objects.get(name= u_name)
            amt = request.POST.get('amount')
            if(acc):
                acc.balance += Decimal(amt)
                acc.save()
                user = Accounts.objects.get(name=u_name)
                return render(request, 'account/depositsuccess.html', {'user' : user })
            else:
                return render(request, 'account/depositfail.html', {'user' : user})
    else:
        return render(request, 'account/enterdep.html', {})


# Withdrawing Money
def wdr(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('amount'):
            u_name = request.POST.get('name')
            acc = Accounts.objects.get(name=u_name)
            amt = request.POST.get('amount')
            if (acc):
                acc.balance -= Decimal(amt)
                acc.save()
                user = Accounts.objects.get(name=u_name)
                return render(request, 'account/withdrawsuccess.html', {'user': user})
            else:
                return render(request, 'account/withdrawfail.html', {'user': user})
    else:
        return render(request, 'account/enterwdr.html', {})

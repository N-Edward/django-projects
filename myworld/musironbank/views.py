from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Account, Transaction
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
import random
import string

# Create your views here.

#we should generate an account numberfor each user,
def generate_account_number():
    start_number = '55' + ''.join(random.choices(string.digits, k=8))
    return start_number

User = settings.AUTH_USER_MODEL 

@receiver(post_save, sender=User)
def create_account(created, instance, sender, **kwargs):
    if created:
        transfer_pin = instance.transfer_pin
        account_status = 'Active'
        account_type = 'Savings'
        fixed_deposit = 'Regular'
        account_number = generate_account_number()
        #create an account model autoamatically
        Account.objects.create(
            user=instance,
            account_number=account_number,
            account_type=account_type,
            account_status=account_status,
            fixed_deposit = fixed_deposit, 
            transfer_pin=transfer_pin,
            account_balance = 0
        )


def transfer(request):
    if request.method == 'POST':
        account_number = request.POST['account_number']
        amount= (request.POST['amount'])
        superuser_account = Account.objects.get(user='superuser username') # set this username to the admin username or your preferred account.
        sender_account = Account.objects.get(user=request.user)
        receiver_account = Account.objects.get(account_number=account_number)
        
        interest_rate = 0.02
        deduction = amount * interest_rate
        
        if sender_account.account_balance >= amount:
            sender_account.account_balance -= amount
            sender_account.save()
            
            receiver_account.account_balance += amount
            receiver_account.save()
            
            Transaction.objects.create (
                sender = request.user,
                receiver = receiver_account.user,
                amount = amount,
                account_number = account_number
            )
            return HttpResponseRedirect ('Transfer')
        else:
            HttpResponse("Insufficinet Funds")
            return HttpResponseRedirect('Transfer')
        
        
    return render(request, 'Transfer')
        
        

def index(reques):
    account = Account.objects.all().values()
    return HttpResponse("Welcome to Musiron Bank")
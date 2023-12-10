from django.db import models

# Create your models here.

class Account(models.Model):
    Account_Type = (('Savings', 'savings'),('Current','current'))
    Account_Status = (
        ('Active','active'),
        ('Closed','closed'),
        ('Frozen', 'frozen')
    )
    Fixed_Deposit = (
        ('Regular', 'regular'),
        ('Senior Citizen', 'senior citizen'),
        ('Corporate','corporate')
    )
    
    user = models.ForeignKey( 'Account',on_delete=models.CASCADE)
    account_number = models.IntegerField(editable=False)
    account_balance = models.DecimalField(max_digits=6, decimal_places=3)
    account_type = models.CharField(max_length=50, choices=Account_Type)
    account_status = models.CharField(max_length=50, choices=Account_Status)
    fixed_deposit = models.CharField(max_length=50, choices=Fixed_Deposit)
    transfer_pin = models.IntegerField()
    
class Transaction(models.Model):
    amount = models.DecimalField(max_digits=6, decimal_places=3, editable=False)
    account_number = models.IntegerField()
    sender = models.ForeignKey("Account", on_delete=models.CASCADE, related_name='who_send')
    receiver = models.ForeignKey('Account', on_delete=models.CASCADE, related_name='who_reciever')
    timestamp = models.DateTimeField(auto_now_add=True)
from django.db import models

# Create your models here.
class Member(models.Model):
    acc_no = models.CharField(max_length=100,unique=True)
    name = models.CharField(max_length=100) 
    balance = models.FloatField(default = 0.0)


    # def add_amount(self, amount):
    #     self.balance += amount
    #     self.save()

    # def withdraw_amo(self, amount):
    #     if self.balance >= amount:
    #         self.balance -= amount
    #         self.save()
    #     else:
    #         return "Insufficient balance"



    def __str__(self):
        return f'{self.acc_no} {self.balance}'



   
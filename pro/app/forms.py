from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['acc_no', 'name', 'balance']
        widgets = {
            'acc_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Account Number'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'balance': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Balance'}),
        }

# from django import forms

# class TransactionForm(forms.Form):
    
    
#     amount = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))


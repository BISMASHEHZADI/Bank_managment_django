from django.shortcuts import render, HttpResponse,redirect
from .models import Member
from .forms import MemberForm # Ensure TransactionForm is imported

# Create your views here.
def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MemberForm()
    st = Member.objects.all()
    return render(request, 'add_member.html', {'form': form, 'stu': st})

# def withdraw(request, acc_no):
#     model = get_object_or_404(Member, acc_no=acc_no)
#     if request.method == 'POST':
#         form = TransactionForm(request.POST)
#         if form.is_valid():
#             if model.withdraw_amo(form.cleaned_data['balance']):
#                 return redirect('add_member')
#             else:
#                 return HttpResponse('Insufficient balance')
#     else:
#         form = TransactionForm()
#     return render(request, 'withdraw.html', {'form': form, 'member': model})

def add_money(request):
    if request.method == 'POST':
        try:
            acc_no = request.POST.get('acc_no')
            amount = request.POST.get('amount')
            member = Member.objects.get(acc_no=acc_no)
            member.balance += float(amount)
            member.save()
            return redirect('add_member')
        except Member.DoesNotExist:
            return HttpResponse('Account not found')

       
    return render(request, 'add_money.html')
    
def withdraw(request):
    if request.method == 'POST':
        acc_no = request.POST.get('acc_no')
        amount = request.POST.get('amount')
        try:
            member = Member.objects.get(acc_no=acc_no)
            if member.balance >= float(amount):
                member.balance -= float(amount)
                member.save()
                return redirect('add_member')
            else:
                return HttpResponse('Insufficient balance')
        except Member.DoesNotExist:
            return HttpResponse('Member not found')
    return render(request, 'withdraw.html')

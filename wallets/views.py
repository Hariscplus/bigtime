from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserWallet

@login_required
def user_wallets(request):
    wallets = UserWallet.objects.filter(user=request.user)
    return render(request, 'wallets/user_wallets.html', {'wallets': wallets})
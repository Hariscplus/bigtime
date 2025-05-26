from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import UserWallet, SupportedCurrency
from .utils import generate_bitcoin_wallet, generate_ethereum_wallet

User = get_user_model()

@receiver(post_save, sender=User)
def create_default_wallets(sender, instance, created, **kwargs):
    if created:
        active_currencies = SupportedCurrency.objects.filter(is_active=True)

        for currency in active_currencies:
            if currency.currency_type == 'fiat':
                UserWallet.objects.create(user=instance, currency=currency, balance=0.0)
            elif currency.currency_type == 'crypto':
                if currency.code == 'BTC':
                    address, private_key = generate_bitcoin_wallet()
                elif currency.code == 'ETH':
                    address, private_key = generate_ethereum_wallet()
                else:
                    continue

                wallet = UserWallet.objects.create(
                    user=instance,
                    currency=currency,
                    balance=0.0,
                    wallet_address=address
                )
                wallet.set_private_key(private_key)
from django.db import models
from django.contrib.auth import get_user_model
from cryptography.fernet import Fernet
from django.conf import settings

User = get_user_model()
fernet = Fernet(settings.ENCRYPTION_KEY.encode())

class SupportedCurrency(models.Model):
    CURRENCY_TYPE_CHOICES = [
        ('fiat', 'Fiat'),
        ('crypto', 'Cryptocurrency'),
    ]

    name = models.CharField(max_length=50, help_text="The name of the currency (e.g., US Dollar, Bitcoin).")
    code = models.CharField(max_length=10, unique=True, help_text="The currency code (e.g., USD, BTC, ETH).")
    currency_type = models.CharField(
        max_length=10,
        choices=CURRENCY_TYPE_CHOICES,
        help_text="Type of the currency (fiat or cryptocurrency)."
    )
    is_active = models.BooleanField(default=True, help_text="Whether this currency is currently active.")

    def __str__(self):
        return f"{self.name} ({self.code})"

class UserWallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wallets", help_text="The user who owns this wallet.")
    currency = models.ForeignKey(SupportedCurrency, on_delete=models.CASCADE, help_text="The currency associated with this wallet.")
    balance = models.DecimalField(max_digits=20, decimal_places=8, default=0.0, help_text="Current balance in the wallet.")
    wallet_address = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Wallet address for cryptocurrency (only applicable for crypto wallets)."
    )
    encrypted_private_key = models.TextField(
        blank=True,
        null=True,
        help_text="Encrypted private key for cryptocurrency wallets."
    )
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the wallet was created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Timestamp when the wallet was last updated.")

    class Meta:
        unique_together = ('user', 'currency')

    def __str__(self):
        return f"{self.user.username} - {self.currency.code} Wallet"

    def set_private_key(self, private_key):
        self.encrypted_private_key = fernet.encrypt(private_key.encode()).decode()
        self.save()

    def get_private_key(self):
        if not self.encrypted_private_key:
            return None
        return fernet.decrypt(self.encrypted_private_key.encode()).decode()
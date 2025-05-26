from django.db import models

class PaymentGateway(models.Model):
    GATEWAY_TYPE_CHOICES = [
        ('fiat', 'Fiat'),
        ('crypto', 'Cryptocurrency'),
    ]

    name = models.CharField(max_length=100, unique=True, help_text="Name of the payment gateway (e.g., PayPal, Stripe, Bitcoin).")
    gateway_type = models.CharField(
        max_length=10,
        choices=GATEWAY_TYPE_CHOICES,
        default='fiat',
        help_text="Type of the payment gateway (fiat or cryptocurrency)."
    )
    module_path = models.CharField(
        max_length=255,
        help_text="Python module path to the gateway integration logic (e.g., 'payments.gateways.stripe')."
    )
    is_active = models.BooleanField(default=True, help_text="Indicates if the gateway is active and available for use.")
    api_key = models.CharField(max_length=255, blank=True, null=True, help_text="API key for the payment gateway (if applicable).")
    secret_key = models.CharField(max_length=255, blank=True, null=True, help_text="Secret key for the payment gateway (if applicable).")
    additional_config = models.JSONField(blank=True, null=True, help_text="Additional configuration for the gateway (e.g., webhook URLs).")

    def __str__(self):
        return self.name

    def get_gateway_handler(self):
        """
        Dynamically loads the gateway handler class based on the module_path.
        """
        import importlib
        try:
            module = importlib.import_module(self.module_path)
            return module.GatewayHandler(self)
        except (ImportError, AttributeError) as e:
            raise ImportError(f"Failed to load gateway handler for {self.name}: {e}")


class PaymentTransaction(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('cancelled', 'Cancelled'),
    ]

    gateway = models.ForeignKey(PaymentGateway, on_delete=models.CASCADE, related_name="transactions", help_text="The payment gateway used for this transaction.")
    transaction_id = models.CharField(max_length=255, unique=True, help_text="Unique identifier for the transaction.")
    amount = models.DecimalField(max_digits=20, decimal_places=8, help_text="Transaction amount.")
    currency = models.CharField(max_length=10, help_text="Currency code (e.g., USD, EUR, BTC, ETH).")
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending',
        help_text="Status of the transaction."
    )
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the transaction was created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Timestamp when the transaction was last updated.")
    metadata = models.JSONField(blank=True, null=True, help_text="Additional metadata related to the transaction (e.g., customer details).")

    def __str__(self):
        return f"{self.gateway.name} - {self.transaction_id}"
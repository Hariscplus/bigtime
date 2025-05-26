import stripe

class GatewayHandler:
    def __init__(self, gateway):
        """
        Initialize the handler with the PaymentGateway instance.
        """
        self.gateway = gateway
        self.api_key = gateway.api_key
        stripe.api_key = self.api_key

    def create_payment(self, amount, currency, metadata=None):
        """
        Create a payment using the Stripe API.
        """
        try:
            payment_intent = stripe.PaymentIntent.create(
                amount=int(amount * 100),  # Stripe uses the smallest currency unit
                currency=currency,
                metadata=metadata or {}
            )
            return payment_intent
        except stripe.error.StripeError as e:
            raise Exception(f"Stripe payment creation failed: {e}")
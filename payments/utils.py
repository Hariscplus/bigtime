from django.shortcuts import get_object_or_404
from .models import PaymentGateway

def process_payment(gateway_id, amount, currency, metadata=None):
    # Get the payment gateway
    gateway = get_object_or_404(PaymentGateway, id=gateway_id, is_active=True)

    # Load the gateway handler dynamically
    handler = gateway.get_gateway_handler()

    # Create the payment
    try:
        payment_response = handler.create_payment(amount, currency, metadata)
        return payment_response
    except Exception as e:
        raise Exception(f"Payment processing failed: {e}")
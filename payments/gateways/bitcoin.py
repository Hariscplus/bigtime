class GatewayHandler:
    def __init__(self, gateway):
        """
        Initialize the handler with the PaymentGateway instance.
        """
        self.gateway = gateway
        self.wallet_address = gateway.additional_config.get("wallet_address")

    def create_payment(self, amount, currency, metadata=None):
        """
        Generate a payment request for Bitcoin.
        """
        return {
            "wallet_address": self.wallet_address,
            "amount": amount,
            "currency": currency,
        }
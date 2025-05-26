from django.http import JsonResponse
from .utils import process_payment

def test_payment(request):
    gateway_id = request.GET.get('gateway_id')  # Pass the gateway ID as a query parameter
    amount = float(request.GET.get('amount', 0))
    currency = request.GET.get('currency', 'USD')

    try:
        response = process_payment(gateway_id, amount, currency)
        return JsonResponse({"success": True, "response": response})
    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)})
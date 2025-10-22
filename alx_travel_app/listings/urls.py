from django.urls import path
from .views import InitiatePaymentAPIView, VerifyPaymentAPIView

app_name = "payments"

urlpatterns = [
    path("payments/initiate/", InitiatePaymentAPIView.as_view(), name="initiate"),
    path("payments/verify/", VerifyPaymentAPIView.as_view(), name="verify"),
]

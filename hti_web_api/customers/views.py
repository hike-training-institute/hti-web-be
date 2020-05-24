from rest_framework import generics
from .serializers import CustomerRequestedQuoteSerializer

class CustomerRequestedQuoteView(generics.CreateAPIView):
    serializer_class = CustomerRequestedQuoteSerializer




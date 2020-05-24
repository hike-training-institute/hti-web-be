from rest_framework import serializers
from .models import CustomerRequestedQuote

class CustomerRequestedQuoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerRequestedQuote
        fields = ['name', 'email', 'phone_number', 'course_interested']
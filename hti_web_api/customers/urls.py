from django.urls import path
from . import views

urlpatterns = [
    path('customer-requested-quote/', views.CustomerRequestedQuoteView.as_view(), name='customer-requested-quote'),
]
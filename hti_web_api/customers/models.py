from django.db import models
import django

class CustomerRequestedQuote(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)
    name = models.CharField(db_column='name', max_length=50, unique=False, blank=False, null=False)
    email = models.EmailField(db_column='email', blank=True, null=False)
    phone_number = models.CharField(db_column='phone_number', max_length=10, blank=False, null=True)
    course_interested = models.CharField(db_column='course_interested', max_length=200, unique=False, blank=False, null=False)
    created_time = models.DateTimeField(db_column='created_time', blank=False, null=False,
                                        default=django.utils.timezone.now)
    modified_time = models.DateTimeField(db_column='modified_time', blank=False, null=False,
                                         default=django.utils.timezone.now)
    deleted_time = models.DateTimeField(db_column='deleted_time', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'customer_requested_quote'
        ordering = ['id']
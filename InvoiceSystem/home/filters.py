import django_filters
from home.models import *
class CustomerFilter(django_filters.FilterSet):
    class Meta:
        model=Customers
        fields=['name','email']
       
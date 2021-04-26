import django_filters

from .models import *


#in use
class FilterContacts(django_filters.FilterSet):
    contact_name_fields = django_filters.CharFilter(method='filter_by_contact_name_fields', label=False)

    class Meta:
        model = Contact
        fields = []
    
    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
        super(FilterContacts, self).__init__(data=data, queryset=queryset, request=request, prefix=prefix)
        self.filters['contact_name_fields'].field.widget.attrs.update({'class': 'search-form'})

    def filter_by_contact_name_fields(self, queryset, name, value):
            return queryset.filter(
            Q(first_name__icontains=value) | Q(last_name__icontains=value)
        )
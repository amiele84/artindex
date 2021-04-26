import django_filters

from .models import *


            ##drop-down filters##

#on each piece list view
#subheader of pieces container

#status: Unfinished, Complete, Sold, Shipping
class AvailabilityFilter(django_filters.FilterSet):
    availability_filter = django_filters.CharFilter(field_name='availability', lookup_expr='iexact')

    class Meta:
        model = NewPiece
        fields = ['availability_filter']

#location: gallery
class LocationFilter(django_filters.FilterSet):
    pass

#date: ordered by date uploaded
class DateFilter(django_filters.FilterSet):
    pass

#medium: what piece is made from
class MediumFilter(django_filters.FilterSet):
    pass

#price: price of piece
class PriceFilter(django_filters.FilterSet):
    pass

#collections: which collections its in 
class CollectionFilter(django_filters.FilterSet):
    pass



            ##Tag Filter##

#user-entered queries
#larger search bar in header of pieces list container
class TagFilter(django_filters.FilterSet):
    pass

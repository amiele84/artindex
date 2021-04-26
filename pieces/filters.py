import django_filters

from .models import *




##main search filter on Add Edit
#currently only has title & subject_matter
class FilterAllPieceFields(django_filters.FilterSet):
    multi_name_fields = django_filters.CharFilter(method='filter_by_all_name_fields', label=False)

    class Meta:
        model = NewPiece
        fields = []
    
    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
        super(FilterAllPieceFields, self).__init__(data=data, queryset=queryset, request=request, prefix=prefix)
        self.filters['multi_name_fields'].field.widget.attrs.update({'class': 'search-form'})

    def filter_by_all_name_fields(self, queryset, name, value):
            return queryset.filter(
            Q(title__icontains=value) | Q(subject_matter__icontains=value)
        )


##in use##
##tags and title
class FilterTags(django_filters.FilterSet):
    tags_name_fields = django_filters.CharFilter(method='filter_by_all_name_fields', label=False)

    class Meta:
        model = NewPiece
        fields = []
    
    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
        super(FilterTags, self).__init__(data=data, queryset=queryset, request=request, prefix=prefix)
        self.filters['tags_name_fields'].field.widget.attrs.update({'class': 'search-form'})

    def filter_by_all_name_fields(self, queryset, name, value):
        if value:
            tags = [tag.strip() for tag in value.split(',')]
            qs = queryset.filter(tags__name__in=tags
#                Q(title__in=tags) | Q(tags__name__in=tags)
                ).distinct()

        return qs

#        return queryset.filter(
#            Q(title__icontains=value) | Q(tags__name__icontains=value)
#        )



##single test filter
#would be for sorting buttons on Add Edit
class FilterSinglePieceField(django_filters.FilterSet):
    multi_name_fields = django_filters.CharFilter(method='filter_by_all_name_fields')

    class Meta:
        model = NewPiece
        fields = []

    def filter_by_all_name_fields(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) | Q(subject_matter__icontains=value)
        ) | queryset.filter(
            Q(title__icontains=value) | Q(subject_matter__icontains=value)
        )

## filter location: gallery
#try setting widget to be a button for filtering
class LocationFilter(django_filters.FilterSet):
    location_filter = django_filters.CharFilter(field_name='location', lookup_expr='iexact')

    class Meta:
        model = NewPiece
        fields = ['location_filter']
    

##end of in use##

##test
#taken from: https://stackoverflow.com/questions/48799668/how-do-i-pass-only-current-user-data-to-be-filtered-in-django-filter/48800338
class CollectionFilter(django_filters.FilterSet):

    class Meta:
        model = NewPiece
        fields=[]

    @property
    def qs(self):
        parent = super().qs
        uploader = getattr(self.request, 'user', None)
        
        if uploader==NewPiece.uploader:
            return parent.filter(uploader=uploader)







            ##drop-down filters##

#on each piece list view
#subheader of pieces container

#status: Unfinished, Complete, Sold, Shipping
class AvailabilityFilter(django_filters.FilterSet):
    availability_filter = django_filters.CharFilter(field_name='availability', lookup_expr='iexact')

    class Meta:
        model = NewPiece
        fields = ['availability_filter']


##main filter on Add Edit views 
from django.db.models import Q
import django_filters

class FilterAllPieceFields_test(django_filters.FilterSet):
    q = django_filters.CharFilter(method='my_custom_filter')

    class Meta:
        model = NewPiece
        fields = ['q']

    def my_custom_filter(self, queryset, name, value):
        return NewPiece.objects.filter(
            Q(artist__iexact=value) | Q(title__iexact=value)
        )


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

##test title search
class ArtistFilter(django_filters.FilterSet):
    artist_filter = django_filters.CharFilter(field_name='artist', lookup_expr='iexact')

    class Meta:
        model = NewPiece
        fields = ['artist_filter']
from django_filters import rest_framework as filters
from vitrines.models import Vitrines


class VitrinesFilter(filters.FilterSet):
    hotel_name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Vitrines
        fields = ['hotel_name']

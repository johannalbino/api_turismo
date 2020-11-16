from rest_framework.serializers import ModelSerializer
from vitrines.models import Vitrines, Country, Category, City


class VitrinesSerializer(ModelSerializer):

    class Meta:
        model = Vitrines
        fields = '__all__'


class CountrySerializer(ModelSerializer):

    class Meta:
        model = Country
        fields = '__all__'


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class CitySerializer(ModelSerializer):

    class Meta:
        model = City
        fields = '__all__'

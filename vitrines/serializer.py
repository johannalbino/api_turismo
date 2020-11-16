from rest_framework.serializers import ModelSerializer
from vitrines.models import Vitrines, Country, Category, City


class CountrySerializer(ModelSerializer):

    class Meta:
        model = Country
        fields = ['country_name', 'slug', 'country_code']


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ['category_name', 'slug']


class CitySerializer(ModelSerializer):

    class Meta:
        model = City
        fields = ['city_name', 'slug', 'state']


class VitrinesSerializer(ModelSerializer):
    city = CitySerializer(many=False)
    country = CountrySerializer(many=False)
    category = CategorySerializer(many=False)

    class Meta:
        model = Vitrines
        fields = ['hotel_name', 'slug', 'image', 'city', 'country', 'category', 'price']
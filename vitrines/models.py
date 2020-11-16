from django.db import models


class City(models.Model):

    city_name = models.CharField("Nome da cidade")
    slug = models.CharField("SLUG")
    state = models.CharField("Estado")
    neighborhood = models.CharField("Bairro")

    class Meta:
        db_table = 'city'


class Country(models.Model):

    country_name = models.CharField("Nome do País")
    slug = models.CharField("SLUG")
    country_code = models.IntegerField(max_length=4)

    class Meta:
        db_table = 'country'


class Category(models.Model):

    category_name = models.CharField("Nome da categoria")
    slug = models.CharField("SLUG")

    class Meta:
        db_table = 'category'


class Vitrines(models.Model):

    hotel_name = models.CharField("Nome do hotel")
    slug = models.CharField("SLUG")
    image = models.URLField("URL Imagem")
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    price = models.DecimalField("Preço", decimal_places=2, max_digits=10)

    class Meta:
        db_table = 'vitrines'

from django.db import models


class Country(models.Model):

    country_name = models.CharField("Nome do País", max_length=100)
    slug = models.CharField("SLUG", max_length=155)
    country_code = models.IntegerField()

    class Meta:
        db_table = 'country'


class City(models.Model):

    city_name = models.CharField("Nome da cidade", max_length=255)
    slug = models.CharField("SLUG", max_length=155)
    state = models.CharField("Estado", max_length=40)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)

    class Meta:
        db_table = 'city'


class Category(models.Model):

    category_name = models.CharField("Nome da categoria", max_length=255)
    slug = models.CharField("SLUG", max_length=155)

    class Meta:
        db_table = 'category'


class Vitrines(models.Model):

    hotel_name = models.CharField("Nome do hotel", max_length=255)
    slug = models.CharField("SLUG", max_length=155)
    image = models.URLField("URL Imagem")
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    price = models.DecimalField("Preço", decimal_places=2, max_digits=10)

    class Meta:
        db_table = 'vitrines'

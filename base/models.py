from django.db import models


class Book(models.Model):
    """

    """
    name = models.CharField(max_length=255)
    price = models.FloatField()
    author = models.ForeignKey("Author")


class Author(models.Model):
    """

    """
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

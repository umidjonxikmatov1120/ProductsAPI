from django.db import models

class ProductsModel(models.Model):
    title = models.CharField(max_length=255)
    articul = models.CharField(max_length=100)
    cloth = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    image = models.ImageField()
    size = models.CharField(max_length=10)
    material = models.CharField(max_length=100)

    def __str__(self):
        return self.title

from django.db import models


class Depense(models.Model):

    title = models.CharField(max_length=200)
    quantity = models.DecimalField(max_digits=10, decimal_places=3)
    desc = models.TextField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
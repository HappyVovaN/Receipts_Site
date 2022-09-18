from django.db import models

# Create your models here.
class Product(models.Model):
    short_name=models.CharField(max_length=50)
    full_name=models.CharField(max_length=200)
    cost=models.FloatField()
    amount=models.IntegerField()
    category=models.CharField(max_length=50)
    shop=models.CharField(max_length=200)
    adress=models.CharField(max_length=200)
    time_date=models.DateTimeField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['full_name', 'time_date'], name='unique_full_name_time_date'
            )
        ]
    def __str__(self):
        return self.full_name
from django.db import models

class Currency(models.Model):
    usd = models.IntegerField()
    rub = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

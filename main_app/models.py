from django.db import models
from django.urls import reverse

# Create your models here.
class Deal(models.Model):
    company_name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    asking_price = models.IntegerField()
    revenue = models.IntegerField()
    sde = models.IntegerField()
    status = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)
    created_on = models.DateField()

    def __str__(self):
        return self.company_name
    
    def get_absolute_url(self):
        return reverse('deal-detail', kwargs={'deal_id': self.id})
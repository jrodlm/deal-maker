from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


STATUS = (
    ('E', 'Expressed Interest'),
    ('L', 'Letter of Intent'),
    ('D', 'Due Diligence'),
    ('N', 'Not for Me'),
    ('P', 'Pass by Seller'),
)

class Deal(models.Model):
    company_name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    asking_price = models.IntegerField()
    revenue = models.IntegerField()
    sde = models.IntegerField()
    status = models.CharField(
        max_length=1,
        choices=STATUS,
        default=STATUS[0][0]
    )
    notes = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.company_name
    
    def get_absolute_url(self):
        return reverse('deal-detail', kwargs={'deal_id': self.id})
    
    def __str__(self):
        return f"{self.get_status_display()}"
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
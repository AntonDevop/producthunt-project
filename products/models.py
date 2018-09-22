from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    votes_total =  models.PositiveIntegerField(default = 1)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    body = models.TextField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def __str__(self):
        return self.title

class Vote(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)

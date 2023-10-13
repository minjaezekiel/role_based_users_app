from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.urls import reverse
# M Enterprises
# LightOne

class User(AbstractUser):
    is_merchant = models.BooleanField('Merchant', default=False)
    
    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
    
class MerchantManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(is_merchant=True)
    
    
class Merchant(User):
    objects = MerchantManager()
    
    class Meta:
        proxy = True
    

    def save(self, *args, **kwargs):
        self.is_merchant = True
        return super().save(*args, **kwargs)

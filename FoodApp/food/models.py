from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Item(models.Model):
    item_name=models.CharField(max_length=100)
    item_desc=models.CharField(max_length=100)
    item_price=models.IntegerField()
    item_image=models.CharField(max_length=500,default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQBdCjb_D9bJ_4_LV04BCn7mLHzwimVycKFsQ&s")


    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})
    